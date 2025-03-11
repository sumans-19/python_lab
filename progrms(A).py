1}
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# # Input from the user
# number = int(input("Enter a number: "))

# # Output result
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")




num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


2}
word = input("Enter a word: ")
count = 0
for char in word:
    count += 1

print(f"Length of the word: {count}")

is_palindrome = True
for i in range(count // 2):
    if word[i].lower() != word[count - i - 1].lower():
        is_palindrome = False
        break

if is_palindrome:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")






def find_length(word):
    count = 0
    for char in word:
        count += 1
    return count



def is_palindrome(word):
    length = find_length(word)  # Reuse the length function
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True

# Main Code
word = input("Enter a word: ")

# Display results
print(f"Length of the word: {find_length(word)}")

if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")



3}
sentence = input("Enter a sentence: ")

# Counting words without .split()
count = 0
in_word = False

for char in sentence:
    if char != ' ' and not in_word:
        count += 1
        in_word = True
    elif char == ' ':
        in_word = False

print(f"Number of words in the sentence: {count}")



sentence = input("Enter a sentence: ")

# Counting words using .split()
words = sentence.split()  # Splits by default on whitespace
count = len(words)

print(f"Number of words in the sentence: {count}")




4}
    # Function to calculate the sum of numbers in a list
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Taking list input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Display result
print(f"Sum of the numbers in the list: {calculate_sum(numbers)}")


# numbers = list(map(int, input("Enter numbers separated by commas: ").split(',')))
# print(numbers)
  



5}
phonebook = {}

n = int(input("Enter the number of contacts: "))

for i in range(n):
    name = input(f"Enter name of person {i + 1}: ")
    number = input(f"Enter {name}'s phone number: ")
    phonebook[name] = number

search_name = input("\nEnter the name to search for their phone number: ")

if search_name in phonebook:
    print(f"{search_name}'s phone number is: {phonebook[search_name]}")
else:
    print(f"{search_name} not found in phonebook.")




6}
# Open the source file for reading
with open("source.txt", "r") as source_file:
    lines = source_file.readlines()

# Open the destination file for writing
with open("odd_lines.txt", "w") as dest_file:
    for i in range(len(lines)):
        if i % 2 == 0:  # Odd lines (0-based index)
            dest_file.write(lines[i])

print("Odd lines have been successfully copied to 'odd_lines.txt'.")






7}
# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input from the user
number = int(input("Enter a number: "))

# Display result
print(f"{number} is {check_even_odd(number)}.")






8}
# Function to count character occurrences
def count_characters(string):
    char_count = {}  # Dictionary to store counts

    for char in string:  # Loop through each character
        if char in char_count:
            char_count[char] += 1  # Increment count if already exists
        else:
            char_count[char] = 1  # Initialize count if first occurrence

    return char_count

# Input from user
text = input("Enter a string: ")

# Function call and output display
result = count_characters(text)

# Display the character count
for char, count in result.items():
    print(f"'{char}' occurs {count} times.")
