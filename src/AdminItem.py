#!/usr/bin/python

# import required modules

# class definition
class AdminItem:
    def __init__(self, d, b, s, a):
        self.date = d[:2]+'/'+d[2:4]+'/'+d[4:6]
        self.batch = '_'+b
        self.seq = int(s)
        self.amt = int(a)/100.0

    def getItem(self):
        return self.date, self.batch, self.seq, self.amt

# main function
def main():
    # function debugging here
    a = AdminItem('041114', '03093', '02550', '0000013664')
    print a.getItem()

# call to main function
if __name__ == '__main__':
    main()
