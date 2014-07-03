#!/usr/bin/python

# import required modules
import sys
from ReturnItem import *
from Constants import CONSTANTS

# class definition
class ItemReader:
    
    # class variable
    itemList = []
    
    def __init__(self, fName):
        
        C = CONSTANTS()
        
        file = open(fName)
        
        for line in file:
            if line[:C.end_pos(0)] == '05':
                ri = ReturnItem(line[C.start_pos(1):C.end_pos(1)],
                            line[C.start_pos(2):C.end_pos(2)],
                            line[C.start_pos(3):C.end_pos(3)],
                            line[C.start_pos(4):C.end_pos(4)],
                            line[C.start_pos(5):C.end_pos(5)],
                            line[C.start_pos(6):C.end_pos(6)],
                            line[C.start_pos(7):C.end_pos(7)],
                            )
                self.itemList.append(ri)
                
        file.close()
                
    def printList(self):
        for item in self.itemList:
            print item.getItem()
            
    def getTotal(self):
        total = 0.0
        for item in self.itemList:
            amt = item.getItem()[3]
            total += amt
        
        return total

# main function
def main():
    # function debugging here
    if len(sys.argv) > 1:
        fileNames = sys.argv[1:]
        for fileName in fileNames:
            ir = ItemReader(fileName)
    else:
        ir = ItemReader('File.txt')
    ir.printList()
    
# call to main function
if __name__ == '__main__':
    main()