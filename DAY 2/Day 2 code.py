while True :

    N = int(input("Enter any number N : "))

    for row in range(N) :
        
        for col in range(N - row) :        # Range can also be written as : range(row , N)
            print(" " , end = "")

        for col in range(row + 1) :
            print("*" , end = "")

        for col in range(row) :
            print("*" , end = "")

        print()
