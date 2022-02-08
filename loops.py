#Basic - Print all integers from 0 to 150.
for x in range(0,151):
    print(x)
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,1000,5):
    print(x)
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,100):
    print(x)
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0 # declearing the sum to zero
for x in range (1, 500000): # for every value between zero and 500,000
    if x % 2 != 0: # checkin if the value is odd
        sum = sum + x # add it to the sum
print(sum)

sum2 = 0
for x in range (1, 500000, 2):
    sum2 += x
print(sum2)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for x in range (2018, 0, -4):
 print(x)

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 60 
highNum = 180
mult = 9

for x in range (lowNum, highNum, mult):
    print(x)

