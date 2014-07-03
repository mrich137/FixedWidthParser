#!/usr/bin/python

# import required modules

# class definition
class ReturnItem:
    def __init__(self, cn, rt, ca, amt, rdata, sa, pd, rtc):
        self.PC_NO = cn
        self.RT = rt
        self.C_ACCT = ca
        self.AMT = int(amt)/100.0
        self.R_DATA = rdata
        self.S_ACCT = sa
        self.P_DATE = pd
        self.RTC = rtc

    def getItem(self):
        return (self.PC_NO, self.RT, self.C_ACCT, self.AMT, self.R_DATA, 
            self.S_ACCT, self.P_DATE, self.RTC)

# main function
def main():
    # function debugging here
    a = ReturnItem('00000000101', '03100050', '000001010291741', '00000005231',
        '000000000132104488', '04426255778', '12/02/13', '1180')
    print a.getItem()

# call to main function
if __name__ == '__main__':
    main()
