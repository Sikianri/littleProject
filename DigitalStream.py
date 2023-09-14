"""黑客帝国数字流"""

import random, shutil, sys, time

#创建常量 
MIN_STREAM_LENGTH = 6 
MAX_STREAM_LENGTH = 24
PAUSE = 0.08
STREAM_NUMBERS = [chr(i) for i in range(48, 58)]# Adds '0' to '9'
STREAM_CHARS = [chr(i) for i in range(32, 126) if chr(i) not in STREAM_NUMBERS] 
COLORS = [
    '\033[91m',
    '\033[92m',
    '\033[93m',
    '\033[94m',
    '\033[95m',
    '\033[96m',
]
RESET = '\033[0m'
#密度范围为0.0 ~ 1.0
DENSITY = 0.025 # 每列刷新字符的概率为0.025
NUMBERS = 0.8 # 显示数字的概率为0.8
CHARS = 0.2 # 显示字符的概率为0.2

#获取终端窗口的大小。
WIDTH = shutil.get_terminal_size()[0]
#如果不自动添加换行符， 我们无法输出Windows上的最后一列
#所以宽度-1
WIDTH -= 1
print('Digital Stream(数字流)')
print('Press Ctrl-C to quit.(按Ctrl-C退出)')
time.sleep(1)

def print_stream():
    color = random.choice(COLORS)
    if random.random() <= NUMBERS: # 根据概率输出数字和字符
        print(color + random.choice(STREAM_NUMBERS) + RESET, end='')
    else:
        print(color + random.choice(STREAM_CHARS) + RESET, end='')
                    

try:
    #对于每一列，如果计数器的值为0，则不显示流;如果计数器的值不为0，则其值表示1或0在列中显示的次数
    columns = [0] * WIDTH
    while True:
        # 为每一列设置计数器
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    #重新启动此列上的流
                    columns[i] = random.randint(MIN_STREAM_LENGTH,
                                                MAX_STREAM_LENGTH)
                    
            # 显示空格或1/0 字符：
            if columns[i] >  0:
                print_stream()
                columns[i] -= 1
            else:
                print(' ', end='')
        print() # 在 columns的行末尾输出一个空行
        sys.stdout.flush() # 确保文本出现在屏幕上
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit() #按CTRL-c结束
