#!/usr/bin/python

# import required modules

# class definition
class ReturnItem:

    def calcCkDigit(self, rt):
        r = [int(c) for c in rt]
        g1 = 7 * (int(r[0]) + int(r[3]) + int(r[6]))
        g2 = 3 * (int(r[1]) + int(r[4]) + int(r[7]))
        g3 = 9 * (int(r[2]) + int(r[5]))
        cdv = (g1 + g2 + g3) % 10
        return rt+str(cdv)

    def __init__(self, cn, rt, ca, amt, sa, pd, rtc):
        self.PC_NO = cn
        self.RT = self.calcCkDigit(rt)
        self.C_ACCT = ca
        self.AMT = int(amt)/100.0
        self.S_ACCT = sa
        self.P_DATE = pd
        self.RTC = rtc

    def getItem(self):
        return (self.PC_NO, self.RT, self.C_ACCT, self.AMT, 
            self.S_ACCT, self.P_DATE, self.RTC)

# main function
def main():
    # function debugging here
    a = ReturnItem('00000000101', '11100002', '000001010291741', '00000005231',
        '04426255778', '12/02/13', '1180')
    print a.getItem()

# call to main function
if __name__ == '__main__':
    main()
