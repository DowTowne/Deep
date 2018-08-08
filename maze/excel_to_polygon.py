 # -*- coding:utf-8 -*-
 # 加载Excel处理包
import xlrd
import arcpy

# #workspace
# 唐涛：这个工作空间是不是放
 # 置所有的shape文件和xlsx文件的地方？你没有交待清楚
arcpy.env.workspace = r"E:\DeepResearch"
# excel file path
excelPath = r"polygon2.xls"
# excel's table index
excelTableIndex = 0
# out file
outName = r"polygon.shp"
# get excel
excel = xlrd.open_workbook('polygon2.xls')
# get table by sheets index
table = excel.sheets()[0]
# number of table's row
nrows = table.nrows
array = arcpy.Array()
point = arcpy.Point()
# #设置坐标系 CGCS2000_3_Degree_GK_Zone_38，这一步设置完成后最终的shp还是会提示坐标系有问题
#唐涛：你这个坐标系统确定是国家2000的吗？不是1980的38度带吗？
spRef = arcpy.SpatialReference(4526)

polygonGeometryList = []
# 这部分是网上找到的代码生成polygon和point的，我把两组合并了一下
# 生成的polygon的shp没有图像，但是单独生成point的shp是合适的
for i in range(1, nrows):
    x = table.cell(i, 0).value
    y = table.cell(i, 1).value
    point.X = float(x)
    point.Y = float(y)
	
	#唐涛：下面这个用j实现的循环，我没有看懂，你为何要这么做！
    for j in point:
        xy = j.split(',')
        print xy[0]
        print xy[1]
        print '\n'
        point.X = float(xy[0])
        point.Y = float(xy[1])
    array.add(point)
    polygon = arcpy.Polygon(array)
    polygonGeometryList.append(polygon)
    array.removeAll()
arcpy.CopyFeatures_management(polygonGeometryList, "E:\\DeepResearch\\polygon.shp")
