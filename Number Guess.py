import random
a = [0,1,2,3,4,5,6,7,8,9]
b = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
d = random.choice(a)
e = random.choice(b)
f = random.choice(b)
print("Difficulty levels: Easy, Moderate or Extreme")
m = input("Enter your difficulty: ")
print("You have 3 lives to guess the number")
i = 0
if m == "Easy" or m == "easy":
    print("Guess between 0-9")
    while i<3:
        n = int(input("Enter your number: "))
        if n < d:
            print("Think Higher")
        elif n > d:
            print("Think lower")
        else:
            print("Perfect guess")
        i+=1    
    if i == 3 and n!=d:
         print("You are out of lives, The answer was:",d,"Better luck next time")      
elif m == "Moderate" or m == "moderate":
    print("Guess between 0-20")
    while i<3:
        
        n = int(input("Enter your number: "))
        if n < e:
            print("Think Higher")
        elif n > e:
            print("Think lower")
        else:
            print("Perfect guess")
        i+=1    
    if i == 3 and n!=e:
         print("You are out of lives, The answer was:",e,"Better luck next time")       
else:
    print("Guess between 0-20")
    while i<3:
        n = int(input("Enter your number: "))
        if n < e:
            if n%2!=0 and e%2==0:
                print("Think Higher and even")
            elif n%2==0 and e%2!=0:
                print("Think Higher and odd")  
            else:
                print("Think Higher")    
        elif n > e:
            if n%2!=0 and e%2==0:
                print("Think Lower and even")
            elif n%2==0 and e%2!=0:
                print("Think Lower and odd") 
            else:
                print("Think Lower")
        else:
            print("Perfect guess")
        i+=1    
    if i == 3 and n!=e:
         print("You are out of lives, The answer was:",e,"Better luck next time")    
print("Thank you for playing")    