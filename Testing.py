# -*- coding: utf-8 -*-
from TaichungAPIUrl import *
#Q : Write to utf-8 file in python
#Source : http://stackoverflow.com/questions/934160/write-to-utf-8-file-in-python
import codecs

size = len(oldAPIList)
formatResult = codecs.open("FormatCheckLog.txt","w","utf-8")
urlNotCompleteCounter = 0

for index in range(size):
	oldAPI = oldAPIList[index]
	newAPI = newAPIList[index]

	e, a, l, f, url = compareAPIFormat(oldAPI,newAPI,formatResult)

	urlNotCompleteCounter += 0 if (l + f) == 0 else 1

if urlNotCompleteCounter == 0:
	print "ALL CLEAR"
else:
	print "%d Files not complete" % (urlNotCompleteCounter,)

formatResult.close()



contentResult = codecs.open("ContentCheckLog.txt","w","utf-8")

for index in range(size):
	oldAPI = oldAPIList[index]
	newAPI = newAPIList[index]

	compareAPIContent(oldAPI,newAPI,contentResult)

contentResult.close()
