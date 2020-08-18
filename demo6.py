#python连接redis导出redis的数据
import redis
import json
import os
import sys
import xlsxwriter
class connectRedis():
	def __init__(self):
		self.host = '192.168.0.103'
		self.port = '6379'
		self.auth = 'jk201148'
		self.r = redis.Redis(host=self.host, port=self.port, password=self.auth,decode_responses=True)
	def existskey(self,keyname):
		return self.r.exists(keyname)
	def getvalue(self):
		valuelist = []
		Keys = connectRedis().r.keys()
		for i in Keys:
			if '需要找的key' in str(i):
				value = json.loads(eval(connectRedis().r.get(i)))
				valuelist.append([value['值1'],value['值2']])
		return valuelist
def write_excel_xlsx(value):
    rootpath = os.getcwd()
    path = os.path.join(rootpath,'token.xlsx')
    newxlsx = xlsxwriter.Workbook(path)
    newsheet = newxlsx.add_worksheet()
    for i in range(0,len(value)):
        for j in range(len(value[1])):
            newsheet.write(i-1,j,str(value[i][j]))
    newxlsx.close()
    print("xlsx格式表格写入数据成功！")
write_excel_xlsx(connectRedis().getvalue())