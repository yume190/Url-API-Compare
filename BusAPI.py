# -*- coding: utf-8 -*-
import urllib2
from urlparse import urlparse
import os
import xmltodict, json
import re
import copy

statusEqual = "E"
statusLack = "L"
statusAdd = "A"

pattern = r"[-+]?[0-9]*\.?[0-9]+"
first = lambda array: None if len(array) == 0 else array[0]

class BusAPI:
	def __init__(self,url,paths = []):
		self.url = url
		self.json = self.getJson()
		for path in paths:
			self.json = self.json[path]
			"""
			if self.json.has_key(path):
				self.json = self.json[path]
			else:
				self.json = []
		if type(self.json) is dict:
			self.json = [self.json]
			"""
		self.keys = [] if len(self.json) == 0 else self.json[0].keys()

	def getJson(self):
		stringData = urllib2.urlopen(self.url).read()

		stringData = self.processJsonp(stringData)

		jsonData = {}
		if self.isJson():
			jsonData = json.loads(stringData)
		elif self.isXml():
			jsonString = json.dumps(xmltodict.parse(stringData))
			jsonData = json.loads(jsonString)

		return jsonData

	def getKeys(self):
		return copy.deepcopy(self.keys)

	def getExtension(self):
		mUrlParse = urlparse(self.url)
		mPath = mUrlParse.path
		mFileName, mFileExtension = os.path.splitext(mPath)

		return mFileExtension

	def isJson(self):
		if self.getExtension() == '.json':
			return True
		return False

	def isXml(self):
		if self.getExtension() == '.xml':
			return True
		return False

	def processJsonp(self,string):
		if len(string) == 0:
			return ''

		if string[0] == "(":
			string = string[1:]
		if string[-1] == ")":
			string = string[:-1]

		return string

class BusAPINew(BusAPI):
	def __init__(self,url,paths = [],keysForSearch = []):
		BusAPI.__init__(self,url,paths)

		newJson = {}
		mPointer = newJson
		for item in copy.deepcopy(self.json):

			mPointer = newJson

			for index, key in enumerate(keysForSearch):

				if len(keysForSearch) == (index + 1):
					mPointer.setdefault(item[key],item)
				else:
					mPointer.setdefault(item[key],{})

				mPointer = mPointer[item[key]]
				del item[key]

		self.jsonForCompare = newJson

class BusAPIOld(BusAPI):
	def __init__(self,url,paths = [],keysDontNeed = []):
		BusAPI.__init__(self,url,paths)

		self.keysDontNeed = keysDontNeed

		self.keysForCompare = copy.deepcopy(self.keys)
		for key in keysDontNeed:
			self.keysForCompare.remove(key)


def saveFileWithString(fileName,string):
	file = open(fileName,"w")
	file.write(string)
	file.close


def compareAPIFormat(oldAPI,newAPI,filePointer):

	fileBlank = "==================== %s ====================" % (oldAPI.url,)
	filePointer.write("\n"+fileBlank+"\n")

	equalCounter = 0
	addCounter = 0
	lackCounter = 0

	valueFormatNotEqualList = []

	oldAPIKeys = oldAPI.getKeys()
	newAPIKeys = newAPI.getKeys()

	for key in oldAPIKeys:
		if key in newAPIKeys:
			#Equal
			mLog = "%s %s" % (statusEqual, key)
			filePointer.write(mLog+"\n")
			equalCounter += 1
			newAPIKeys.remove(key)

			if type(oldAPI.json[0][key]) is not type(newAPI.json[0][key]):
				#Format Not Equal
				mLog = "Key %s : %s != %s" % (key,type(oldAPI.json[0][key]),type(newAPI.json[0][key]))
				valueFormatNotEqualList.append(mLog)

		else:
			#Lack
			mLog = "%s %s" % (statusLack, key)
			filePointer.write(mLog+"\n")
			lackCounter += 1

	for key in newAPIKeys:
		#Add
		mLog = "%s %s" % (statusAdd, key)
		filePointer.write(mLog+"\n")
		addCounter += 1

	if len(valueFormatNotEqualList) == 0 :
		filePointer.write("Clear")
	else:
		for mLog in valueFormatNotEqualList:
			#print mLog
			filePointer.write(mLog+"\n")

	result = (equalCounter, addCounter, lackCounter, len(valueFormatNotEqualList), oldAPI.url)
	#E Key Equal
	#A New API Add key
	#L New API Lack key
	#F Format Not Equal, when has the same key, Ex : {"ID":"1"} VS {"ID":1}
	print "L:%d \t F:%d \t E:%d\t A:%d\t Url:%s" % (lackCounter, len(valueFormatNotEqualList), equalCounter, addCounter, oldAPI.url)
	return result

def compareAPIContent(oldAPI,newAPI,filePointer):

	fileBlank = "==================== %s ====================" % (oldAPI.url,)
	filePointer.write("\n"+fileBlank+"\n")

	for oldItem in oldAPI.json:
		try:
			newItem = newAPI.jsonForCompare
			for key in oldAPI.keysDontNeed:
				newItem = newItem[oldItem[key]]

			for key in oldAPI.keysForCompare:
				oldNumber = first([round(float(x),4) for x in re.findall(pattern,oldItem[key])])
				newNumber = first([round(float(x),4) for x in re.findall(pattern,newItem[key])])
				if oldNumber != None and newNumber != None and oldNumber == newNumber:
					continue

				if newItem[key] != oldItem[key]:
					filePointer.write("Key %s : '%s' '%s'\n" % (key, oldItem[key],newItem[key]))

		except KeyError as e:
			errorLog = "Error Type  : Key Error, key : {0} not found.".format(e)
			filePointer.write(errorLog + "\n")

		except:

			errorLog = "\n==================== Error Start ====================\n"
			for key in oldAPI.keysDontNeed:
				errorLog += "%s:'%s' " % (key,oldItem[key])
			errorLog += "\nold:%s" % (oldItem,)
			errorLog += "\nnew:%s" % (newItem,)
			errorLog += "\n===================== Error End =====================\n"
			filePointer.write(errorLog + "\n")

if __name__ == '__main__':
	pass
