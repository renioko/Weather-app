# challenge #1:
# Write the pseudocode and create flowchart that finds the next ‘n’ number of leap years from current year. 
# (Here ‘n’ is the input taken from user.)
# //This problem would require you to create two flowcharts, one demonstrating a function that tells you whether it is a year is leap year or not and the other to loop incrementally until you find next ‘n’ leap years.//
# 
# Write the pseudocode and create flowchart that finds the next ‘n’ number of leap years from current year. 

# def leap_year_check(year):
#     if year % 400 == 0:
#         print(f'Hoorray! {year} is a leap year!')
#         return year

#     elif year % 4 == 0:
#         print(f'Hoorray! {year} is a leap year!')
#         return year
#     else:
#         while year:
#             if year % 4 != 0:
#                 year += 1
#             else:
#                 print(f"The next leap year is {year}.")
#                 return year

# def produce_leap_years(n):
#     year = input('enter a year: ')
#     year = (int(year)) 
#     leap_year = leap_year_check(year)
#     n-1
#     if n > 0:
#         print('Next leap years:')
#     while n > 0:
#         leap_year += 4
#         n -= 1
#         print(leap_year)

# produce_leap_years(5)

# ============================
#  challenge #5:

# Find the second largest number in an array and demonstrate the workflow using pseudocode and flowchart.

# Example: 
# Given an input array [45, 62, 8, 90, 13, 54, 7], the output should be 62.

# INPUT: array (i.e. [45, 62, 50, 20, 5])
# biggest-number = CALCULATE-MAX(from array)  
# array = REMOVE-biggest-number(from array)  
# result = CALCULATE-MAX(from array)
# PRINT: "the second biggest number is: ", result

# array = [45, 62, 50, 20, 5]
# biggest_number = max(array)
# print(biggest_number)
# array.remove(biggest_number)
# print(array)
# result = max(array)
# print(result)


#  =============================
# challenge #4:
# Show the workflow of removing all occurrences of a given character from the input string using pseudocode and flowchart.

# EXAMPLE: 
# Removing all of the “s” from “Mississippi” will return “Miiippi”

# !!!!! IMPORTANT: 

# This solution treats capital letters as different character than lower letters: 

# EXAMPLE: 

# Input: ‘Kawasaki” , character to remove: ‘k’ => result: ‘Kawasai’ 

# Input: “kawasaki1” character to remove: ‘k’ => result: ‘awasai1’  

# INPUT: text
# INPUT: given-character
# IF LENGTH( of given-character) != 1:
# PRINT: 'error, you can enter only one character"
# END 
# ELSE:
# FOR character IN text:
# IF character == given-character:
# REMOVE character (from text) 
# ELSE: CONTINUE
# //loop continues//
# END FOR
# PRINT: text (now we have text with removed all occurences of given-character)
# END

text = input('enter text:')
character = input('enter character to remove: ')

if len(character) != 1:
    print('error! too many characters')

for char in text:
    if char == character:
        new_text = text.replace(char, '')
    else:
        pass
print(new_text)

# LEPSZA WERSJA:
# ====
# INPUT: text
# INPUT: given-character
# IF LENGTH( of given-character) != 1:
# PRINT: 'error, you can enter only one character"
# END 
# ELSE:
# INITIALIZE: str: result = ""
# FOR character IN text:
# IF character != given-character:
# result += char
# //loop continues//
# END FOR
# PRINT: result (now we have text with removed all occurences of given-character)
# END

text = input('enter text:')
character = input('enter character to remove: ')

if len(character) != 1:
    print('error! too many characters')

result = ''
for char in text:
    if char != character:
        result += char

print(result)




# ===========================
# challenge #3:
# Using a flowchart and pseudocode, show the workflow of code that can tell if a number is deficient, perfect or abundant. 

# A whole number is said to be deficient if the sum of proper divisors is less than the number.
# (e.g. 8 is deficient as 1+2+4 < 8

# A number is perfect if the sum of proper divisors is equal to the number.
# (e.g. 6 is perfect because 1+2+3=6)

# A number is called abundant if the if the sum of the proper divisors is greater than the number.
# (e.g. 12 is abundant as 1+2+3+4+6 > 12).

# ==============================
# challenge #2:
# Write the pseudocode and create a flowchart that demonstrate the workflow of identifying if a number is an Admirable number or not. 

# A whole number is admirable if the sum of proper divisors (excluding the number itself) minus two times one the proper divisors is equal to the number.

# Here’s an example- 30 is an admirable number because 1+2+3+5+6+10+15 – 2*6 = 30.
