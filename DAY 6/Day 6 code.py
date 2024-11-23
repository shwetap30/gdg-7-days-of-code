def count_vowel(s) :
    vowels = set("aeiouAEIOU")

    count = 0
    for char in s :
        if char in vowels:
            count += 1
    return count

input_string = input("Enter the string : ")
print(count_vowel(input_string))
