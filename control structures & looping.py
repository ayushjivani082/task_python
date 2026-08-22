num = float(input("Enter a number : " ))

if num > 0 :
   print("Positive")
elif num < 0 :
    print("Negative")
else :
    print("Zero")




marks = float(input("Enter your mark : "))


if marks >= 90 :
    print("Grade A")
elif marks >= 75 :
    print("Grade B")
elif marks >= 60 :
    print("Grade C")
else :
    print("Grade D")




day = int(input("Enter day number (1-7) : "))

match day :
    case 1 : print("Monday")
    case 2 : print("Tuesday")
    case 3 : print("Wednesday")
    case 4 : print("Thursday")
    case 4 : print("Firday")
    case 5 : print("Saturday")
    case 5 : print("Sunday")
    case _:
        print("Invaild day")




num = int(input("Enter a number : "))

i = 1

while i <= 10 :
    print(num , "X" , i , "=" , num * i)
    i += 1




for i in range (2 , 101 , 2):
    print(i , end=" ")




rows = int(input("Enter number of rows : "))

for i in range (1 , rows + 1) :
    for j in range (rows - i) :
        print("  " , end= "")
    for j in range (2 * i - 1) :
        print("*" , end= "")
        print()





fixed_number = 7

for i in range(9) :
    guess = int(input("Guess the numbar : "))

    if guess == fixed_number :
        print("Correct! You guessed the number. ")
        break
    elif guess < fixed_numbre :
        print("Too low!")
    else :
        print("Too high! ")
    if i == 2 :
        print("sorry! You used all 3 tried. ")

        
              


print("Prime numbers between 1 and 50 :")

for num in range(2 , 51) :
    is_prime = True
    for i in range(2 , num) :
        if num % i == 0 :
            is_prime = False
            break
        if is_prime :
            print(num , end= " ")
















        
        







        
