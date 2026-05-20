# control structures - decides the flow of the program

# conditional statements - used to make decisions based on a condition

'''if False:
    print("Statement is true")
else:
    print("Statement is false")'''
    
'''
Javascript :
if (true) {
    console.log("Statement is true)
} else {
    console.log("Statement is false)
}
'''

# nested conditions
'''if True:
    if True:
        print("Statement 1")
    else:
        print("Statement 2")
else:
    print("Statement 3")'''
    
# elif statements
'''if True:
    print("Statement 1")
elif True:
    print("Statement 2")
else:
    print("Statement 3")'''
    
# number = 21
    
'''if number > 0:
    print("Positive")
else:
    print("Not positive")'''
    
'''if number > 0:
    if number % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Not positive")'''
    
'''if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Neither positive nor negative")'''
    
# Looping - allows to repeat a code multiple times
# 2 types of loops - for and while

'''for num in range(2, 10, 2):
    print(num)'''
    
'''for number in range(1, 11):
    if number % 2 == 0:
        print("Even")
    else:
        print("odd")'''
        
'''number = 1

while number <= 10:
    print(number)
    number += 1'''
    
# nested loops - loop inside loop
'''for j in range(6):
    for i in range(5):
        print("*", end=" ")
    print()'''

# else with looops
'''number = 5
while number < 10:
    print(number)
    number += 1
else:
    print("loop ended")'''
    
# Jumping statements - used to change the normal flow of the control flow statements
# break, continue, pass

'''for i in range(10):
    if i == 5:
        pass
    print(i)'''
    
# Program to find the prime numbers between a range of numbers
start = 30
end = 40

for number in range(start, end+1):
    flag = True
    for i in range(2, number ** 0.5):
        if number % i == 0:
            print("Not prime")
            flag = False
            break
        
    if flag:
        print("Prime")