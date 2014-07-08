#!/usr/bin/python

# import required modules
import sys
from ItemReader import *
from Constants import CONSTANTS

# class definition
class ItemWriter:

    
    
    def writeLine(self):
        line = '+{:-^10}+{:-^8}+{:-^7}+{:-^16}+\n'
        line = line.format('','','','')
        self.outFile.write(line)
    
    def writeHeader(self):
        
        h = CONSTANTS().get_fields()
        self.outFile.write('| {:^8} | {:^6} | {:^4} | {:^14} |\n'
            .format(h[0],h[1],h[2],h[3]))
    
    def __init__(self, fName, itemReader):
        self.outFile = open(fName, 'w')
        
        itemList = itemReader.itemList
        
        self.amt = itemReader.getTotal()
        
        self.writeLine()
        self.writeHeader()
        
        for item in itemList:
            i = item.getItem()
            self.writeLine()
            self.outFile.write('| {:^8} | {:^6} | {:>4} | {:>14,.2f} |\n'
                .format(i[0],i[1],i[2],i[3]))
        
        self.writeLine()
        self.outFile.write('\n# ITEMS: {}'.format(len(itemReader.itemList)))
        self.outFile.write('\nTOTAL: {:,.2f}'.format(itemReader.getTotal()))
        self.outFile.close()

# main function
def main():
    # function debugging here
    if len(sys.argv) > 1:
        outFileNames = sys.argv[1:]
        for outFileName in outFileNames:
            ir = ItemReader(outFileName)
    else:
        ir = ItemReader('test.ack')
    
    iw = ItemWriter('test.rpt', ir)
    
# call to main function
if __name__ == '__main__':
    main()