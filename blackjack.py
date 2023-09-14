"""21点小游戏 该版本没有分牌或者保险
规则:https://baike.baidu.com/item/21%E7%82%B9%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99/15541720
"""

import random, sys

# 创建常量
HEARTS = chr(9829) # 字符 9829 表示 黑桃
DIAMONDS = chr(9830) # 字符9830表示 黑方块
SPADES = chr(9824) # 字符9824表示 
CLUBS = chr(9827) #字符9827表示
BACKSIDE = 'backside'


def main():
    print('''21点小游戏,该版本没有分牌或者保险''')

    money = 5000
    while True: # 主循环
        if money <= 0:
            print("你出局了！")
            print("好消息是你没有用真钱玩")
            print("感谢游玩！")
            sys.exit()

    # 让玩家输入这一轮的点数
        print('Money:', money)
        bet = getBet(money)

        # 给庄家和玩家各发两站牌
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # 处理玩家的动作
        print('Bet:', bet)
        while True: # 保持循环，直到玩家停牌或者爆掉
            displayHands(playerHand, dealerHand, False)
            print()

            # 检查玩家牌的点数是否超过21点：
            if getHandValue(playerHand, dealerHand, False) > 21:
                print()
                break
            
            # 获取玩家的下一步操作， 即拿牌(H) 、 停牌(S)或加倍(D)
            move = getMove(playerHand, money - bet)

            # 处理玩家的动作
            if move == 'D':
                # 玩家将点数加倍
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}. '.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                # 选择另一张牌或者点数加倍
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank,suit))
                playerHand.append(newCard)

                



def getBet(maxBet):
    return bet


def getDeck():
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):


def getHandValue(cards):
    return value


def displayCards(cards):
    print(row)

def getMove(playerHand, money):

    return move