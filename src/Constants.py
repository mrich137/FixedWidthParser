'''
Created on Jul 1, 2014

@author: Matt
@module: Constants
'''

# import base class
from ConstBaseClass import *


class CONSTANTS(ConstBaseClass):
    """ Constant Group 1 """
    def __init__(self):
        """ Constructor to define group1 constants """
        
        # DEFINE CONSTANTS HERE
        self.FLAG   = (0,   2)
        self.DATE   = (2,   6)
        self.BATCH  = (8,   5)
        self.SEQ    = (13,  5)
        self.AMOUNT = (27,  10)
        
        
        
        ''' Uncomment this line to prevent adding more attributes '''
        #self._locked = 1
     
        
    def start_pos(self, field):
        for item in self.items():
            if item[0] == field:
                return item[1][0]
        return None
        
    
    def end_pos(self, field):
        for item in self.items():
            if item[0] == field:
                return item[1][0] + item[1][1]
        return None

        
def main():
    """ main function for module debug """
    AC = CONSTANTS()
    print AC.items()
    AC.printitems()
 
    print AC.start_pos('FLAG')
    print AC.end_pos('FLAG')   
    
    print AC.start_pos('DATE')
    print AC.end_pos('DATE')
    
    print AC.start_pos('BATCH')
    print AC.end_pos('BATCH')
    
    print AC.start_pos('SEQ')
    print AC.end_pos('SEQ')
    
    print AC.start_pos('AMOUNT')
    print AC.end_pos('AMOUNT')

              
if __name__ == '__main__':
    main()