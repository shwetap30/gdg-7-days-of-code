n = int(input("Enter the size of your array : "))
input_numbers = input("Enter space-separated integers : ")

array = list(map(int , input_numbers.split()))

positive_num_sum = 0

for num in array :

    if (num > 0) :
        positive_num_sum += num

print("The sum of positive numbers of array is : " , positive_num_sum)
