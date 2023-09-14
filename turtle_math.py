import math
import turtle

# 用海龟画一个圆
def drawCircleTurtle(x, y, r):
    # 移动到圆的开始
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    # 画一个圆
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))

drawCircleTurtle(100, 100, 50)
turtle.mainloop()

# 整个画出来
def draw(self):
    # 绘制其余的点
    R, k, l = self.R, self.k, self.l

    # 遍历0至360*nRot（可能意味着需要旋转的完整圈数）的角度，
    # 步长为self.step，来逐步绘制图案
    for i in range(0, 360*self.nRot + 1, self.step):

        # 将角度从度数转为弧度。
        a = math.radians(i)

        # 使用数学公式计算x和y的坐标。
        x = R*((1-k)*math.cos(a) + 1*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) + 1*k*math.sin((1-k)*a/k))

        # 移动海龟到计算出的x, y坐标位置。
        self.t.setpos(self.xc + x, self.yc + y)

    # 在循环结束、所有的点都被绘制后，隐藏海龟的光标。
    self.t.hideturtle()

    # 更新绘图步骤
    def update(self):
        # 如果已完成绘制, 则直接返回不再进行绘制
        if self.drawingComplete:
            return 
        
        # 增加绘制的角度
        self.a += self.step
        # 获取对象中的某些属性: R, k, l
        R, k, l = self.R, self.k, self.l
        # 将角度从度数转为弧度
        a = math.radians(self.a)

        # 使用数学公式计算x和y的坐标
        x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = self.R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        # 移动海龟到计算出的x, y坐标位置
        self.t.setpos(self.xc+ x, self.yc + y)

        # 如果绘制完成 (即角度大于或等于360度乘以旋转数), 设置完成标志
        if self.a >= 360*self.nRot:
            self.drawingComplete = True

            # 绘制完成，所以隐藏海龟光标    
            self.t.hideturtle()
