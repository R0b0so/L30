
def Roman(Number):
    M = (Number, 'M', 1000)
    CM = (Number, 'CM', 900)
    D = (Number, 'D', 500)
    CD = (Number, 'CD', 400)
    C = (Number, 'C', 100)
    XC = (Number, 'XC', 90)
    L = (Number, 'L', 50)
    XLV = (Number, 'XLV', 45)
    X = (Number, 'X', 10)
    IX = (Number, 'IX', 9)
    V = (Number, 'V', 5)
    IV = (Number, 'IV', 4)
    I = (Number, 'I', 1)
    return M+CM+D+CD+C+XC+L+XLV+X+IX+V+IV+I
Number = int(input("Enter a number from 1 to 1000 "))
print(Roman(Number))
