dictionary = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
    }

while True:
    
    number = input("Enter a number in Roman Numeral: ")
    output = []
    length = len(number)
    for i in range(0, length-1):
        if dictionary[number[i]] < dictionary[number[i+1]]:
            output.append( - dictionary[number[i]])
        else:
            output.append(dictionary[number[i]])
        i = i+1
        
    output = sum(output) + dictionary[number[length-1]]
    print(f"{number} in Roman Numerals means : {output}")