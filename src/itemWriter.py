#!/usr/bin/python

# import required modules
import sys
from ItemReader import *

# class definition
class ItemWriter:
    
    def writeLine(self):
        line = '+{:-^10}+{:-^8}+{:-^6}+{:-^16}+\n'.format('','','','')
        self.outFile.write(line)
    
    def writeHeader(self):
        h = ('DATE','BATCH','SEQ','AMOUNT')
        self.outFile.write('| {:^8} | {:^6} | {:^4} | {:^14} |\n'.format(h[0],h[1],h[2],h[3]))
    
    def __init__(self, fName, iReader):
        self.outFile = open(fName, 'w')
        
        itemList = iReader.itemList
        
        self.amt = iReader.getTotal()
        
        self.writeLine()
        self.writeHeader()
        
        for item in itemList:
            i = item.getItem()
            self.writeLine()
            self.outFile.write('| {:^8} | {:^6} | {:>4} | {:>14,.2f} |\n'.format(i[0],i[1],i[2],i[3]))
        
        self.writeLine()
        self.outFile.write('\n# ITEMS: {}'.format(len(iReader.itemList)))
        self.outFile.write('\nTOTAL: {:,.2f}'.format(iReader.getTotal()))
        self.outFile.close()

# main function
def main():
    # function debugging here
    if len(sys.argv) > 1:
        inFileNames = sys.argv[1:]
        for inFileName in inFileNames:
            ir = ItemReader(inFileName)
            iw = ItemWriter((inFileName +'.rpt'), ir)
    else:
        ir = ItemReader('test.ack')
        iw = ItemWriter('test.rpt', ir)
    
# call to main function
if __name__ == '__main__':
    main()