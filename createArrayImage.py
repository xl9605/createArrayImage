import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def createBlackImg():
    # 创建一个1920x1080的图片,通道为2
    img = np.zeros([1080,1920,3])
    # 显示该图
    cv2.imshow("black",img)
    # 将这个图写入硬盘
    cv2.imwrite("black.jpg",img)
    # cv2.waitKey(0)


def createNumberImage():
    # 设置字体为自己下载的微软雅黑，字号为300
    font = ImageFont.truetype("font/msyh.ttf",300)
    # 字体颜色为白色
    fillColor = (255,255,255)
    # 显示位置
    position = (500,300)
    for i in range(1,9001):
        # 读取一张黑色纯色背景图
        image = cv2.imread("row/black.jpg")
        # 先将图片转换成PIL格式
        image_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        arrayStr = str(i)
        # 将文字写入图片
        draw = ImageDraw.Draw(image_PIL)
        draw.text(position, arrayStr, font=font, fill=fillColor)
        image = cv2.cvtColor(np.asarray(image_PIL), cv2.COLOR_RGB2BGR)
        # cv2.imshow("asdas",image)
        saveFileName = "createArray/" + str(i) + ".jpg"
        print("正在生成第{}张图片.".format(i))
        cv2.imwrite(saveFileName,image)
    # cv2.waitKey(0)


if __name__ == '__main__':
    createNumberImage()
