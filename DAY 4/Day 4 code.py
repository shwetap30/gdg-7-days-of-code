X = int(input("Number of Schools : "))
Y = int(input("Number of Students in each school : "))
Z = int(input("Number of Students passed the exam : "))

Percentage_passed = (Z / (X * Y) ) * 100

if (Percentage_passed > 50 and (X * Y) >= Z) :
    print("Yes")

elif((X * Y) < Z) :
    print("Passed students cannot be greater than total number of students.\nInvalid Values.\nEnter Valid Values")

else :
    print("No")
