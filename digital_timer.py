"""数字时钟
像液晶时钟一样显示时间（可以试着改成辉光钟）
按CTRL-C结束程序
"""

import sys,time
import sevseg # 导入sevseg.py 模块

try:
    while True: # 主循环
        # 通过输出换行符来清空屏幕
        print('\n' * 60)
        # 从计算机的是中获取当前时间
        currentTime = time.localtime()
        # 用12 进行取模，即使用12小时制，而不是24小时
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12' # 12小时制现实的是12.00，而不是0.00
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # 从sevseg 模块中获取数字字符串
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # 显示数字到屏幕
        print(hTopRow + '    ' + mTopRow + '    ' + sTopRow)
        print(hMiddleRow + '    ' + mMiddleRow + '    ' + sMiddleRow)
        print(hBottomRow + '    ' + mBottomRow + '    ' + sBottomRow)
        print()
        print('Press Ctrl + c to quit')

        # 继续循环，直到发生第二次变化
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('数字时钟')
    sys.exit()





