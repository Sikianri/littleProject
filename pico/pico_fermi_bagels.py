""" 
Pico Fermi Bagels 猜数字游戏
一个逻辑推理游戏，你必须根据线索猜数字
"""

import random

NUM_DIGITS = 3  # 可以试着把3设置为1或者10
MAX_GUESSES = 10  # 请试着将10设置为1 或者100


def main():
    print('''Bagels, 一个逻辑推理游戏

我正在想一个没有重复数字的数字{}
请试着猜出它。这是一些规则：
当我说： 意味着：
Pico    一个正确的数字但出现在错误的位置
Fermi   一个正确的数字并出现在正确的位置
Bagels  没有数字正确。

举个例子,如果这个秘密数字是248,而你猜了843。
这就会显示 Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # 主循环
        # secretNum 存储了玩家所要猜测的秘密数字
        secretNum = getSecretNum()
        print('我想了一个数字')
        print(' 你有 {} 次机会猜出它 .'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # 保持循环，知道玩家输入正确的猜测数字
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('猜测 #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # 如果玩家猜对了数字
            if numGuesses > MAX_GUESSES:
                print('你用完了猜测次数')
                print('答案揭晓： {}.'.format(secretNum))

        # 询问玩家是否再想玩一次
        print('你想再玩一次吗? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('感谢游玩!')


def getSecretNum():
    """返回唯一一个长度为NUM_DIGITS且由随机数字组成的字符串"""
    numbers = list('0123456789')  # 创建数字0-9的列表
    random.shuffle(numbers)  # 将他们随机排列

    # 获取秘密数字列表中的前NUM_DIGITS位数字
    secretNum = ''

    
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """返回一个由Pico、Fermi、Bagels组成的字符串,用于猜测一个三位数"""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # 正确的数字位于正确的位置
            clues.append('Fermi ')
        elif guess[i] in secretNum:
            # 正确的数字不在正确的位置
            clues.append('Pico ')
    if len(clues) == 0:
        return 'Bagels'  # 没有正确的数字
    else:
        # 将clues列表按字母顺序排序，使其不会泄露数字的信息
        clues.sort()
        # 返回一个由clues 列表中所有元素组成的字符串
        return ''.join(clues)


# 程序运行入口（如果不是作为模块导入的话）
if __name__ == '__main__':
    main()
