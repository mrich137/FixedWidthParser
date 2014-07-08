'''
Created on Jul 1, 2014

@author: mrich
@module: Constants.ConstBaseClass
'''

""" DO NOT MODIFY BASE CLASS!!!!! """
class ConstBaseClass:
    """
    forbids to overwrite existing variables
    forbids to add new values if "_locked" variable exists
    """
    
    def __setattr__(self,name,value):
        """ Base Class constructor to prevent changing const vals """
        if(self.__dict__.has_key("_locked")):    
            raise NameError("Class is locked can not add any attributes (%s)"%name)
        if self.__dict__.has_key(name):
            raise NameError("Can't rebind const(%s)"%name)
        self.__dict__[name]=value
        
    def islocked(self):
        """ Returns bool of locked status """    
        if(self.__dict__.has_key("_locked")):
            return True
        else:
            return False    
        
    def printitems(self):
        """ Prints names & values for class consts (excludes _locked)"""
        for i in self.__dict__.items():
            if i[0] != '_locked':
                print self.__class__.__name__+ '.'+ i[0], '\t=\t', i[1]
        
        print "Locked:", self.islocked()    
        print '\n'
        
    def items(self):
        """ Returns List of (name, value) """
        return self.__dict__.items()
        
