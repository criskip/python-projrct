#for fizzbuzz in range(1,100):
    #if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        #print("fizzbuzz")
        #continue
    #elif fizzbuzz % 3 == 0:
        #print("fizz")
        #continue
    #elif fizzbuzz % 5 == 0:
        #print("buzz")
        #continue
    #print(fizzbuzz)


num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

for i in range(num1, num2):
    if i %3 == 0 and i %5 == 0:
        print(i, "fizzbuzz")
    elif i %5 == 0:
        print(i, "buzz")
    elif i %3 == 0:
        print(i, "fizz")
    else:
        print("i")

