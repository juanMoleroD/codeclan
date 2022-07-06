# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even = []
for number in numbers:
    if number % 2 == 0: even.append(number)
print(even)
# 2. Print the difference between the largest and smallest value:
sorted_numbers = sorted(numbers)
print(sorted_numbers[-1] - sorted_numbers[0])

# 3. Print True if the list contains a 2 next to a 2 somewhere.
counter = 0
for number in numbers:
    if number == 2: counter += 1
print(counter >= 2)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
sum = 0
skip = False
for number in numbers:
    if skip == False and number != 6:
        sum += number
    if number == 6:
        skip = True
    if number == 7 and skip == True:
        skip = False
print(sum)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

sum2 = 0
counter2 = 0
while counter2 < len(numbers):
    if numbers[counter2] != 13:
        sum2 += numbers[counter2]
        counter2 += 1
    else: 
        counter2 += 2
'''
for i in range(0, len(numbers)):
    print(i)
    if numbers[i] != 13:
        sum2 += numbers[i]
    else: i += 2
'''

print(sum2)



