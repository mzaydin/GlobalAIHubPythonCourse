#Explain your work

#Question 3 ; Day 4
def prime_first(num):
    temp = 0
    for i in range(2,num-1):
        if(num%i == 0):
            temp += 1
    if temp==0:
        print(num)        
        
def prime_second(num):
    prime_first(num)

for i in range(2,100):
    if(i < 500):
        prime_first(i)
    elif(499 < i < 1000):
        prime_second(i)
