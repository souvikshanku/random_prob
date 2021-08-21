dic = {
    9: ("CM", "XC", "IX"),
    8: ("DCCC", "LXXX", "VIII"),
    7: ("DCC", "LXX", "VII"),
    6: ("DC", "LX", "VI"),
    5: ("D", "L", "V"),
    4: ("CD", "XL", "IV"),
    3: ("CCC", "XXX", "III"),
    2: ("CC", "XX", "II"),
    1: ("C", "X", "I"),
    0: ("", "", "")}

while True:
    number = input("Enter a number from 1 to 999:")
    k = len(number) - 1
    j = 0
    output = ""  

    while k >= 0:
        i = int(number[k])
        output = dic[i][2-j] + output 
        k = k-1
        j = j + 1
    
    print(f'{number} in Roman Numeral is: {output}')