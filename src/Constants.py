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
        self.FIELDS    =   ("FLAG", "DATE", "BATCH", "SEQ", "AMOUNT")
        self.FLAG   = (0,   2)
        self.DATE   = (2,   6)
        self.BATCH  = (8,   5)
        self.SEQ    = (13,  5)
        self.AMOUNT = (27,  10)
        
        
        
        ''' Uncomment this line to prevent adding more attributes '''
        #self._locked = 1
     
        
    def start_pos(self, field):
        for item in self.items():
            if item[0] == self.get_field(field):
                return item[1][0]
        return None
        
    
    def end_pos(self, field):
        for item in self.items():
            if item[0] == self.get_field(field):
                return item[1][0] + item[1][1]
        return None

    def get_fields(self):
        for item in self.items():
            if item[0] == 'FIELDS':
                return item[1]

    def get_field(self, field):
        return self.get_fields()[field]

    def get_num_fields(self):
        return len(self.get_fields())

        
def main():
    """ main function for module debug """
    AC = CONSTANTS()
    # print AC.items()
    # AC.printitems()

    print AC.get_num_fields()
    print AC.get_fields()

    print AC.get_field(0)
    print AC.start_pos(0)
    print AC.end_pos(0)
    
    # print AC.start_pos(1)
    # print AC.end_pos(1)
    
    # print AC.start_pos(2)
    # print AC.end_pos(2)
    
    # print AC.start_pos(3)
    # print AC.end_pos(3)
    
    print AC.get_field(4)
    print AC.start_pos(4)
    print AC.end_pos(4)

if __name__ == '__main__':
    main()