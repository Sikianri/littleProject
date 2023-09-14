"""十六进制猜数字和字母游戏，默认猜测3个字符，15次机会！ by: Shiki Yang"""

import random
import sys

numDigits = 3  # 设置默认猜测字符数量
maxGuess = 15 # 设置默认猜测次数


def main():
    setting()
    print(f'''Pico!, 这是一个逻辑推理游戏
    我刚刚从十六进制数\'0123456789ABCDEF\' 中，
    随机选取了{numDigits}位不重复的十六进制数，
    请试着猜出它，字母不分大小写
    下面是一些规则：
    当我说：    意味着：
    Right       一个正确的数字出现在了正确的地方
    Pico        一个正确的数字出现在了不正确的地方
    Bagels      什么都没猜对
        
    举个例子，如果这个秘密16进制数是：3F4， 而你猜了0F3
    这就会显示 Pico Right 
    祝你玩的开心''')

    while True:  # 设置主循环
        secretNum = getSecretNum()  # 获取需要猜出的数字
        print(f"\n我刚刚想了一个数字，你有{maxGuess}次机会猜出它")

        numGuesses = 1
        while numGuesses <= maxGuess:
            while True:  # 获取用户的猜测输入
                guess = input(f"第{numGuesses}次猜测: \n> ") 
                if len(guess) == numDigits and isHex(guess): # 判断用户输入是否合规
                    break
                else:
                    print(f"请输入正确的十六进制{numDigits}位数字(0-9,a-f,A-F)")
                
            if guess.upper() == secretNum:  # 判断用户是否猜中秘密数字
                print("You got it !")
                break
            else :
                print(getClues(guess.upper(), secretNum))  # 打印猜测提示
            # 更新回合次数
            numGuesses += 1
        
        if numGuesses == maxGuess + 1:  # 如果超过回合数未猜中，就公布答案
            print(f"很遗憾你没猜中，秘密数字是{secretNum}")
        # 询问是否需要重新开始游戏
        gameAgain = input("请问你还需要继续玩吗？（yes or no）\n> ")
        if 'y' not in gameAgain.lower():
            break
    print("感谢游玩!\n") 

        

def setting():  # 从命令行获取修改猜测字符数量和猜测次数的改动，如果有
    global numDigits,maxGuess  # 声明是全局变量来修改全局变量的值
    if len(sys.argv) > 2:  # 判断是否提供了两个参数
        try:
            tempNumDigits = int(sys.argv[1])
            tempMaxGuess = int(sys.argv[2])

            # 判断参数范围，是否在调整范围内
            if 1 <= tempNumDigits <= 10 and 1 <= tempMaxGuess <= 100:
                numDigits = tempNumDigits
                maxGuess = tempMaxGuess
            else:
                print("Error: 参数范围不正确，请确保猜测位数处于1-10位，猜测次数处于1-100次")
                sys.exit(1)  # 退出程序，返回错误代码1

        except ValueError:
            print("Error： 请为猜测位数和猜测次数提供整数值")
            sys.exit(1) # 退出程序，返回错误代码1
    

def isHex(guess):
    try:
        int(guess, 16)
        return True
    except ValueError:
        return False


def getSecretNum():
    # 返回一个numDigits位的不重复十六进制数
    Hexs = list('0123456789ABCDEF')
    random.shuffle(Hexs)

    shuffleHex = ''
    for i in range(numDigits):  # 把创建的不重复十六进制数随机排序
        shuffleHex += Hexs[i]  # 把元素添加到返回值

    return shuffleHex


def getClues(guess, secretNum):
    clues = []
    for i in range(len(secretNum)):
        if guess[i] == secretNum[i]:
            # 如果一个正确的数字在正确的位置
            clues.append('Right')
        elif guess[i] in secretNum:
            # 如果一个正确的数字在不正确的位置
            clues.append('Pico')
        
    if len(clues) == 0:
        # 如果没有一个数字正确返回Bagels
        return 'Bagels'
    else:
        clues.sort()  # 把提示按照字母大小排序，防止泄露位置信息
        return ''.join(clues)


if __name__ == '__main__':
    main()


