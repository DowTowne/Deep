#coding:utf-8
#build by LandGrey 2016-05-17

try:
    import pytesseract
    from PIL import Image
except ImportError:
    print "Import Error !"
    raise  SystemExit

img=Image.open("test.jpg")
vcode= pytesseract.image_to_string(img)
print vcode