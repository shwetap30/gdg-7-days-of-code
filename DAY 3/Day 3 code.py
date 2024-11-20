a = int(input("Enter non-negative number1 (a) : "))
b = int(input("Enter non-negative number2 (b) : "))

print()

if (a < b and a >= 0 and b > 0) :

    for num in range(a , b + 1) :


        if (num % 5 == 0 and num % 7 == 0) :
            print("FooBar")

        elif (num % 5 == 0) :
            print("Foo")

        elif (num % 7 == 0) :
            print("Bar")

        else :
           print("Baz")

elif (a > b) :
    print("a is Greater than b.\nPlease enter the numbers in a VALID RANGE.")

elif (a == b) :
    print("Both a and b are Equal.\nPlease enter the numbers in a VALID RANGE.")

else :
    print("Enter a NON-NEGATIVE INTEGER / INTEGERS.")
