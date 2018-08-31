"""
	Prod Archive DC
"""

import pyodbc
from os.path import join

try:
	cn = pyodbc.connect('DRIVER={SQL Server};SERVER=xx.xx.xx.xx;DATABASE=[db];UID=[usr];PWD=[pwd]')
	#cn = pyodbc.connect('DRIVER={SQL Server};SERVER=xx.xx.xx.xx;DATABASE=[db];UID=[usr];PWD=[pwd]')
	prodfile = r"c:\users\david\documents\archive_prods.txt"
	file = open(prodfile, "r")


	for line in file:
		try:
			tSql = "select * from tblProductions where (autProductionID = %s)" % line
			cursor = cn.cursor()
			cursor.execute(tSql)
			rows = cursor.fetchall()
			print "%s success!" % line
		except Exception as e:
			print e
except Exception as e:
	print e