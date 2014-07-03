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
			if line[:C.end_pos('FLAG')] == '25':
				ai = AdminItem(line[C.start_pos('DATE'):C.end_pos('DATE')],
							line[C.start_pos('BATCH'):C.end_pos('BATCH')],
							line[C.start_pos('SEQ'):C.end_pos('SEQ')],
							line[C.start_pos('AMOUNT'):C.end_pos('AMOUNT')]
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