# # -*- coding: utf-8 -*-
# import os
# import sys
# import codecs
# import xlrd
# #http://pypi.python.org/pypi/xlrd
# if len(sys.argv) != 2 :
#     print "argv count != 2, program exit"
#     print "usage: a.py excel filename"
#     exit(0)
# print "excel  to js on"
#     excel filename = sys.argv[1]
# def floattostring (afloat):
#     if type(afloat) != float:
#         return ""
#     strtemp = str(afloat)
#     strlist = strtemp.split(".")
#     if len(strlist) == 1 :
#         return strtemp
#     else:
#         if strlist[1] == "0" :
#             return strlist[0]
#         else:
#             return strtemp
#
# def table2js n(table, js onfilename):
# nrows = table.nrows
# ncols = table.ncols
# f = codecs.open(js onfilename,"w","utf-8")
# f.write(u"{\n\t\"list\":[\n")
# for r in range(nrows-1):
#     f.write(u"\t\t{ ")
#     for c in range(ncols):
#         strcellvalue = u""
#         cellobj = table.cell_value(r+1,c)
#         if type(cellobj) == unicode:
#             strcellvalue = cellobj
#         elif type(cellobj) == float:
#             strcellvalue = floattostring(cellobj)
#         else:
#             strcellvalue = str(cellobj)
#         strtmp = u"\""  + table.cell_value(0,c) + u"\":"+ strcellvalue
#         if c< ncols-1:
#             strtmp += u", "
#         f.write(strtmp)
#     f.write(u" }")
#     if r < nrows-2:
#         f.write(u",")
#     f.write(u"\n")
# f.write(u"\t]\n}\n")
# f.close()
# print "create ",js onfilename," ok"
# return
#
# data = xlrd.open_workbook(excel filename)
# table = data.sheet_by_name(u"tablelist")
# rs = table.nrows
# for r in range(rs-1):
#     print table.cell_value(r+1,0), "==>", table.cell_value(r+1,2)
#     desttable = data.sheet_by_name(table.cell_value(r+1,0))
#     destfilename = table.cell_value(r+1,2)
#     table2js n(desttable,destfilename)
#
# print "all ok"