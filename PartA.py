#lab programs (part A)
#1.prime or not :
# Input the number
num = int(input("Enter a number: "))
# Prime number check
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True  # Assume it's prime initially
    for i in range(2, int(num**0.5) + 1):  # Check divisibility from 2 to sqrt(num)
        if num % i == 0:
            is_prime = False  # If divisible, it's not prime
            break  # No need to check further

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")




#2.claculate length of the string without buitin function and check for pallindrome:
# Input the string
s = input("Enter a string: ")

# Calculate the length of the string manually
length = 0
for char in s:
    length += 1

# Print the length of the string
print("Length of the string:", length)

# Check if the string is a palindrome using slicing
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")






#3.accept a sentence from user and count number of words in the sentence:
sen = input("enter a long sentence:")
word = sen.split()
print(word)
print("number of words are : " , len(word)) 


#4.calculate sum of all the numbers in the list:
nums = [1, 2, 3, 4]
total_sum = 0

for num in nums:
    total_sum += num

print("The sum of all the numbers in the list is:", total_sum)



#5.store phone numbers of people in the dictionary and display when called:
# Create a dictionary to store phone numbers
phone = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}
def display_phone(name):
    if name in phone:
        print(f"{name}'s phone number is: {phone[name]}")
    else:
        print(f"No phone number found for {name}.")

name_to_search = input("Enter the name to search for: ")

display_phone(name_to_search)
