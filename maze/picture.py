#-*-coding:utf-8-*-
#设置系统默认编码，执行dir（sys）时不会看到这个方法，
#在解释器中执行不通过，可以先执行reload(sys)，
#在执行 setdefaultencoding('utf8')，此时将系统默认编码设置为utf8。
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。
#函数time.time()用于获取当前时间戳,
import time
time1 = time.time()
#PIL (Python Image Library) 是 Python 平台处理图片的事实标准
from PIL import Image
# 文字识别引擎，图像识别工具
import pytesseract

#二值化算法，将图像上的像素点的灰度值设置为0或255，
#也就是将整个图像呈现出明显的黑白效果的过程。
#使图像中数据量大为减少，从而能凸显出目标的轮廓。
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img
image = Image.open(r'e:test.jpg')

#去干扰线算法 input:grey image
#这个算法没找到，不清楚这一部分，知道是降噪，就是不明白干了些啥，再研究研究
def depoint(img):
    pixdata = img.load()
    w, h = img.size
    for y in range(1, h-1):
        for x in range(1, w-1):
            count = 0
            if pixdata[x, y-1] > 245:
                count = count + 1
            if pixdata[x, y+1] > 245:
                count = count + 1
            if pixdata[x-1, y] > 245:
                count = count + 1
            if pixdata[x+1, y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x, y] = 255
    return img
#转化为灰度图
img = image.convert('L')
#把图片变成二值图像。黑白、B&W、单色图像表示二值图像。
img1 = binarizing(img, 190)
#img2 = depoint(img1)
img1.show()
code = pytesseract.image_to_string(img1)
#print "识别该验证码是：" + str(code)

