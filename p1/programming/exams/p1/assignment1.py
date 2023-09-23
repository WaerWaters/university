# Daniel Elsborg Johnsen, djohns22@student.aau.dk, cs-22-dvml-1-p1-01
# Programmet er ikke baseret på fælles arbejde i gruppen





# konverterings funktioner
def integer_to_binary(number):
    print(f'{number:08b}')

def integer_to_float(number):
    print(float(number))

def integer_to_roman_numeral(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div = number // num[i]
        number %= num[i]
        while div:
            print(roman[i], end = "")
            div -= 1
        i -= 1

def roman_numeral_to_integer(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    num = 0
    while i < len(s):
        if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
        else:
            num+=roman[s[i]]
            i+=1
    print(num)
    
    
    
# Menu programmet
def menu():
    n = int(input("Choose the amount of options: "))
    options = []

    for n in range(1, n+1):
        options.append(n)
        print(n)

    picked_number = input("Choose an option: ")

    while (picked_number.isdigit() is False) or (int(picked_number) not in options):
        print("please pick a valid option")
        picked_number = input("Choose an option: ")

# Konvertering af heltal til et andet talsystem program  
def convert_integer():
    number = int(input("Pick integer number: "))
    print("1: integer to binary\n2: integer to float\n3: integer to roman numeral")
    picked_conversion = int(input("pick option number: "))
    if picked_conversion == 1:
        integer_to_binary(number)
    elif picked_conversion == 2:
        integer_to_float(number)
    elif picked_conversion == 3:
        integer_to_roman_numeral(number)        

# Konvertering af enten heltal til romer tal eller romer tal til heltal afhængig af om inputtet indeholder et tal program
def conversion_integer_and_roman_numeral():
    num = input("Number to convert: ")
    if any(n.isdigit() for n in num):
        num = int(num)
        integer_to_roman_numeral(num)
    else:
        roman_numeral_to_integer(num)
        

# kaldning af funktionerne/programmerne
#menu()
#convert_integer()
#conversion_integer_and_roman_numeral()