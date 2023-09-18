"""
生日悖论 一个破除错误直觉的概率论知识
探索生日悖论的惊人概率
"""

import datetime
import random

# 创造一个按照月份排序的元组
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

def getBirthdays(numberOfBirthdays):
    """返回一个随即生日日期对象的数字列表"""
    birthdays = []
    for i in range(numberOfBirthdays):
        # 年份对于模拟并不重要，所以我们假设所有生日都在同一天
        startOfYear = datetime.date(2000, 1, 1)

        # 随机获取一年中的同一天
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """返回在生日列表中多次出现的日期对象"""
    if len(birthdays) == len (set(birthdays)):
        return None  # 若所诱僧日都不同，则返回none
    
    # 将这个生日与其他生日进行比较
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  # 返回相同的生日
            

def main():
    print('''生日悖论, by Al Sweigart
    
    这个生日悖论展示了即使在很少的一群人中，生日相同的概率也是惊人的
    该程序会进行多次概率实验，以确定不同规模小组中生日相同的概率
    ''')
    while True:
        print('How many birthdays shall I generate? (Max 100)')
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            numBDays = int(response)
            break  # 玩家输入了有效的总数，结束循环
    print()
    # 显示生成的生日
    print('这是', numBDays, '生日是:')
    birthdays = getBirthdays(numBDays)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            # 每个生日之间用逗号隔开
            print(',' ,end = '')
            monthName = MONTHS[birthday.month - 1]
            dateText = '{} {}'.format(monthName, birthday.day)
            print(dateText, end='')

    print()
    print()

    # 确定是否存在两个相同的生日
    match = getMatch(birthdays)

    # 显示结果
    print('In this simulation, ', end='')
    if match != None:
        monthName = MONTHS[match.month - 1]
        dateText = '{} {}'.format(monthName, match.day)
    else:
        print('there are no matching birthdays.')
    print()

    # 运行 100000 次循环
    print('Generating', numBDays, 'random birthdays 100000 times...')
    input('Press Enter to begin...')

    print('Let\'s run another 100000 simulations.')
    simMatch = 0  # 模拟中有多少相同的生日
    for i in range(100_000):
        # 每100000次模拟后输出当前进度
        if i % 10_000 == 0:
            print(i, 'simulations run...')
        birthdays = getBirthdays(numBDays)
        if getMatch(birthdays) != None:
            simMatch = simMatch + 1
    print('100000 simulations run.')

    # 显示模拟结果
    probability = round(simMatch / 100_000 * 100,2)
    print('Out of 100,000 simulations of', numBDays, 'people, there was a')
    print('that', numBDays, 'people have a', probability, '% chance of')
    print('having a matching birthday in their group.')
    print('That\'s probably more than you would think!')

if __name__ == "__main__":
    main()
