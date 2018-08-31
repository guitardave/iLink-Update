"""
	Prod Archive DC
"""

import pyodbc
from os.path import join

try:
	cn = pyodbc.connect('DRIVER={SQL Server};SERVER=OHMGDEV77\SQLEXPRESS;DATABASE=WizDatabase;UID=wdbusr;PWD=4WizPlayerz')
	#cn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.175;DATABASE=WizDatabase;UID=wdbusr;PWD=4WizPlayerz')
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