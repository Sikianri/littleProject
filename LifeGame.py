"""康威生命游戏，按CTRL+C停止"""

import copy, random, sys, time, shutil

# 创建常量
WIDTH = shutil.get_terminal_size()[0] -1 # 单元格的宽度
HEIGHT = shutil.get_terminal_size()[1] # 单元格的高度

# 可以尝试更改字符
ALIVE = '#' # 代表活细胞的字符
# 尝试更改字符
DEAD = ' ' # 代表死细胞

# cells 额 nextCells 是表示游戏中的状态的字典
# 他们的键是(x, y)元组， 它们的值是ALIVE 或 DEAD
nextCells = {}
# 将随机死细胞和活细胞放入 nextCells 
for x in range(WIDTH): # 循环遍历每个可能的列
    for y in range(HEIGHT): # 循环遍历每隔可能的行
        # 细胞存活或死亡的概率各占50%
        if random.random() > 0.9:
            nextCells[(x, y)] = ALIVE # 添加一个活细胞
        else:
            nextCells[(x, y)] = DEAD # 添加一个死细胞

while True: # 主循环
    # 该循环的每次迭代都是模拟的一个步骤

    #print('\n' * 50) # 用换行符分割每个步骤
    cells = copy.deepcopy(nextCells)

    # 在屏幕上输出单元格
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end = '') # 输出#或空格
        print() # 在行尾输出添加一行空格
    print('Press Ctrl-C to quit.')

    # 根据当前步骤的单元格计算下一步的单元格
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # 获取 (x, y)的相邻坐标，即使它们环绕在边缘
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # 计算四周处于存货状态的细胞的数量
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1 # 左上角存在活细胞
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1 # 正上方存在活细胞
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1 # 右上角存在活细胞
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1 # 左边存在活细胞
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1 # 右边存在活细胞
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1 # 左下角存在活细胞
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1 # 正下方存在活细胞
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1 # 右下角存在活细胞

            # 根据康威生命游戏的规则设置单元格
            if cells[(x, y)] == ALIVE and (numNeighbors == 2
                or numNeighbors == 3):
                    # 有两个或三个的邻居的活细胞保持活动状态
                    nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # 有三个邻居的死细胞变成活细胞
                nextCells[(x, y)] = ALIVE
            else:
                # 其他一切情况都会导致死亡状态或保持死亡状态
                nextCells[(x, y)] = DEAD
                
                
            
    try:
        time.sleep(0.01) # 添加一秒暂停以减少闪烁
    except KeyboardInterrupt:
        print("欢迎来到康威生命游戏")
        sys.exit() # 按CTRL+C ，程序结束
            