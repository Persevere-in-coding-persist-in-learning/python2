# coding=utf-8
"""
计算圆的面积
area=Π*r*r
Version: 0.1
Author: huijz
Date: 2020-08-21
"""
import math

radius = float(input('请输入圆的半径:'))

perimeter = 2 * math.pi * radius

area = math.pi * radius * radius

print '圆的周长:%.2f' % perimeter
print "圆的面积:%.3f" % area
