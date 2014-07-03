#!/usr/bin/python

# import required modules
import sys
from AdminItem import *
from Constants import CONSTANTS

# class definition
class AdminReader:
	
	# class variable
	adminList = []
	
	def __init__(self, fName):
		
		C = CONSTANTS()
		
		file = open(fName)
		
		for line in file:
			if line[:C.end_pos(0)] == '25':
				ai = AdminItem(line[C.start_pos(1):C.end_pos(1)],
							line[C.start_pos(2):C.end_pos(2)],
							line[C.start_pos(3):C.end_pos(3)],
							line[C.start_pos(4):C.end_pos(4)]
							)
				self.adminList.append(ai)
				
		file.close()
				
	def printList(self):
		for item in self.adminList:
			print item.getItem()
			
	def getTotal(self):
		total = 0.0
		for item in self.adminList:
			amt = item.getItem()[3]
			total += amt
		
		return total

# main function
def main():
    # function debugging here
	if len(sys.argv) > 1:
		fileNames = sys.argv[1:]
		for fileName in fileNames:
			ar = AdminReader(fileName)
	else:
		ar = AdminReader('test.ack')
	ar.printList()
	
# call to main function
if __name__ == '__main__':
    main()