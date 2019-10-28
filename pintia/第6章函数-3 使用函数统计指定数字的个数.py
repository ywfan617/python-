def CountDigit(number,digit ):
    strnum=str(number)
    return strnum.count(str(digit))
if __name__ == '__main__':
    res=CountDigit(-21252,2)
    print(res)