#!/usr/bin/python

# import required modules
import sys
from ItemReader import *

# class definition
class ItemWriter:
    
    def writeLine(self):
        line = '+{:-^14}+{:-^11}+{:-^17}+{:-^18}+'.format('','','','')
        self.outFile.write(line)

        line = '{:-^20}+{:-^13}+{:-^10}+{:-^6}+\n'.format('','','','')
        self.outFile.write(line)
    
    def writeHeader(self):
        h = ("PC_NO", "RT", "C_ACCT", "AMT", "R_DATA",
            "S_ACCT", "P_DATE", "RTC")
        
        self.outFile.write(('| {:^12} | {:^9} | {:^15} | {:^16} |')
            .format(h[0],h[1],h[2],h[3]))
        
        self.outFile.write((' {:^18} | {:^11} | {:^8} | {:^4} |\n')
            .format(h[4],h[5],h[6],h[7]))
    
    def __init__(self, fName, iReader):
        self.outFile = open(fName, 'w')
        
        itemList = iReader.itemList
        
        self.amt = iReader.getTotal()
        
        self.writeLine()
        self.writeHeader()
        
        for item in itemList:
            i = item.getItem()
            self.writeLine()
            self.outFile.write(('| {:^12} | {:^9} | {:^15} | {:>16,.2f} |')
                .format(i[0],i[1],i[2],i[3]))
        
            self.outFile.write((' {:^18} | {:^11} | {:^8} | {:^4} |\n')
                .format(i[4],i[5],i[6],i[7]))
        
        self.writeLine()
        self.outFile.write('\n# ITEMS: {}'.format(len(iReader.itemList)))
        self.outFile.write('\nTOTAL: {:,.2f}'.format(iReader.getTotal()))
        self.outFile.close()

# main function
def main():
    # function debugging here
    if len(sys.argv) > 1:
        outFileNames = sys.argv[1:]
        for outFileName in outFileNames:
            ir = ItemReader(outFileName)
    else:
        ir = ItemReader('File.txt')
    
    iw = ItemWriter('test.rpt', ir)
    
# call to main function
if __name__ == '__main__':
    main()