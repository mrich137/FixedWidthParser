#!/usr/bin/python

# import required modules
import sys
from AdminReader import *

# class definition
class AdminWriter:
	
	def writeLine(self):
		line = '+{:-^10}+{:-^8}+{:-^6}+{:-^16}+\n'.format('','','','')
		self.outFile.write(line)
	
	def writeHeader(self):
		h = ('DATE','BATCH','SEQ','AMOUNT')
		self.outFile.write('| {:^8} | {:^6} | {:^4} | {:^14} |\n'.format(h[0],h[1],h[2],h[3]))
	
	def __init__(self, fName, adReader):
		self.outFile = open(fName, 'w')
		
		adList = adReader.adminList
		
		self.amt = adReader.getTotal()
		
		self.writeLine()
		self.writeHeader()
		
		for item in adList:
			i = item.getItem()
			self.writeLine()
			self.outFile.write('| {:^8} | {:^6} | {:>4} | {:>14,.2f} |\n'.format(i[0],i[1],i[2],i[3]))
		
		self.writeLine()
		self.outFile.write('\n# ITEMS: {}'.format(len(adReader.adminList)))
		self.outFile.write('\nTOTAL: {:,.2f}'.format(adReader.getTotal()))
		self.outFile.close()

# main function
def main():
    # function debugging here
	if len(sys.argv) > 1:
		outFileNames = sys.argv[1:]
		for outFileName in outFileNames:
			ar = AdminReader(outFileName)
	else:
		ar = AdminReader('test.ack')
	
	aw = AdminWriter('test.rpt', ar)
	
# call to main function
if __name__ == '__main__':
    main()