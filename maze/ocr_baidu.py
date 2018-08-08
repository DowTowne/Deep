# -*- coding:utf-8 -*-
from aip import AipOcr
#引用对了，但是后面这个import Document不知道哪里错了
#from docx import Document
#个人的秘钥系统，登录百度云开通服务就能获取
APP_ID = '086642fc6b8f42dbb80d5e9cb2d80fc0'
API_KEY = 'f033cf940aa24d6faa94102e010a1d49'
SECRET_KEY = '7362902c03064988bb48b8c7f5dd0084'
#client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#client.basicGeneralUrl(image, options)
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#读取图片后面这个‘rb’是个啥没懂
def get_img (filepath):
   with open(filepath, 'rb') as f:
       return f.read()
#参数选择这个官方文档里有写
options = { 'detect_direction ': 'true ', ' language_type ' : ' CHN_ENG '}
#打开一个word文件
#document = Document()
#从1到2把两张图片循环处理
for p in range(1, 2):
#示例代码这里写到Unicode，是把格式转成标准utf8，但是为什么报错呢？这一个路径怎么读数个图片呢？
#(unicode('C:\Users\Admin\Desktop\A\图片{}.jpg'.format(p) ,"utf8")) 范例是这么写的
   image = get_img(unicode('E:\\qing.png'.format(p), "utf8"))
   result = aipOcr.basicGeneral(image, options)

print result
#for i in range(1, result['words_result_num']):
#在word文档中写入单词结果保存为docx格式
 #   paragraph = document.add_paragraph(result['words_result'][i]['words'])
#document.save('t.docx')

