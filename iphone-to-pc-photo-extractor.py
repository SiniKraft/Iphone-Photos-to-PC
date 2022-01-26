import sqlite3
import os
import shutil
import sys
if sys.platform == "win32":
	os.system("@echo off & title Iphone Backup photo dumper for windows ! & cls")
print("Iphone Backup photo dumper for windows !"
	"\nThis tool is able to copy all photos from an unencrypted Iphone backup made with iTunes.")
if sys.platform == "win32":
	os.system("pause")
print("Checking your backups ... (This can take a while !)")
#for x in range()

conn = sqlite3.connect('Manifest.db')
cur = conn.cursor()
uuid_list = []
alias_list = []
for row in cur.execute('SELECT * FROM Files'):
	if "CameraRollDomain" in str(row):
		uuid_list.append(row[0])
		alias_list.append(row[2])
uuid = ""
for x in range(0, len(uuid_list)):
	uuid = uuid_list[x]
	try:
		print("Total completed : {}%".format(int((x / len(uuid_list)) * 100)))
		print("\nCopying %s to %s ..." % (uuid, alias_list[x]))
		if not os.path.isdir(os.path.dirname(alias_list[x])):
			os.makedirs(os.path.dirname(alias_list[x]))
		shutil.copy(uuid[:2] + "\\" + uuid, alias_list[x])
	except Exception as e:
		print("Failed to copy %s to %s : %s" % (uuid, alias_list[x], str(e)))
if sys.platform == "win32":
	os.system("pause")
