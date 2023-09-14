import random

def get_random_color():
    COLORS = [
        '\033[91m',  # 红色
        '\033[92m',  # 绿色
        '\033[93m',  # 黄色
        '\033[94m',  # 蓝色
        '\033[95m',  # 紫色
        '\033[96m'   # 青色
    ]
    return random.choice(COLORS)

# 演示如何输出彩色数字
for _ in range(100):
    print(get_random_color() + str(random.randint(0, 9)) + '\033[0m', end='')
print()