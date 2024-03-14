# Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.
# Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a zigzag. More formally, your task is to construct an array of length numbers.length - 2, where the ith element of the output array equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.
# Example
# For numbers = [1, 2, 1, 3, 4], the output should be solution(numbers) = [1, 1, 0].
# (numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1;
# (numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3;
# (numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4;
# For numbers = [1, 2, 3, 4], the output should be solution(numbers) = [0, 0];
# Since all the elements of numbers are increasing, there are no zigzags.
# For numbers = [1000000000, 1000000000, 1000000000], the output should be solution(numbers) = [0].
# Since all the elements of numbers are the same, there are no zigzags.
# input
numbers = [1,2,1,3,4]
# expected output = [1,1,0]
def solution(numbers):
    new_arr = []
    # the loop iterates over a range of indices, the loop goes from 0 to len(numbers) - 2 the -2 is used to ensure that there are always three consecutive elements to form a triple 
    for i in range(len(numbers) - 2):
        # now we assign the values of numbers to variables a b and c respectively
        a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]
        # this line checks wehter the current triple satisfies the conditions for the zig zag pattern
        if (a < b and b > c) or (a > b and b < c):
            new_arr.append(1)
        else:
            new_arr.append(0)
    return new_arr
#==============================================================================================


#==============================================================================================
# You are given an array of integers nums. Your task is to determine whether the array contains a "peak" element. A "peak" element is defined as an element that is greater than its neighbors.
# Write a function named has_peak that takes in a list of integers nums and returns True if the array contains a peak element, and False otherwise.
# For example:
# For nums = [1, 2, 3, 1], the function should return True, because 3 is a peak element (greater than both its neighbors).
# For nums = [1, 2, 2, 3], the function should return False, because there are no peak elements in the array.
# Test your function with different input arrays to ensure it works correctly.
# Constraints:
# The length of the array nums will be at least 3.
# The array nums will contain only integers.
# Your task is to write a function has_peak that implements this logic and returns the correct result for various input arrays. Good luck!
#input
nums = [1,3,1]
#expected output:
#True
#first ill create a function called has_peak
# i need to loop over the elements in the array
#in this case we use range and give it the parameters so it starts at 1 because we know that the zero element doesnt have a neigbor to the left, and ends at the lenght of the array so we use len(nums)
#
#ill need an if statement as if one of the elements is bigger than the one to the left or to the right then to return true 
def has_peak(nums):
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return True
    return False
#==============================================================================================


#==============================================================================================
# You are given a two-digit integer n. Return the sum of its digits.
# Example
# For n = 29, the output should be
# solution(n) = 11.
n = 29
def solution(num):
    #the tens place represent the number of tens in a number 
    tens_digit = num // 10
    #the units digit represents the single digits in the numbers 
    unit_digit = num %10
    #then add those together
    result = tens_digit + unit_digit
    return result
#==============================================================================================


#==============================================================================================
#Write a function that returns the sum of two numbers.
def solution(param1, param2):
    return param1 + param2
#==============================================================================================


#==============================================================================================
# Problem Statement:
# You are given a list of integers nums. Your task is to find and return the sum of all positive integers in the list.
# Write a function named sum_positive that takes in a list of integers nums and returns the sum of all positive integers in the list.
# For example:
# For nums = [1, -2, 3, -4, 5], the function should return 9, because the sum of all positive integers [1, 3, 5] is 9.
# For nums = [-1, -2, -3], the function should return 0, because there are no positive integers in the list.
# Test your function with different input arrays to ensure it works correctly.
# Constraints:
# The length of the array nums will be at least 1.
# The array nums will contain both positive and negative integers.
# Your task is to write a function sum_positive that implements this logic and returns the correct result for various input arrays. Good luck! If you need further assistance or clarification on any aspect, feel free to ask.
#first i create the array with positive and negative numbers
#second i create the function and give it nums as a parameter
# i need to iterate through out the array to find the positive and negative numbers
#m
nums = [1, -2, 3, -4, 5]
def sum_positive(nums):
    #new variable to store the positive numbers
    only_positive = 0
    #iterate over each number in the nums array
    for n in nums:
        #if the number is positive we add it to the only positive variable
        if n > 0:
            only_positive += n
    #return the new variable
    return only_positive
#==============================================================================================


#==============================================================================================
# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
# Example
# For year = 1905, the output should be
# solution(year) = 20;
# For year = 1700, the output should be
# solution(year) = 17
year = 1905
#expected output: 20
def solution(year):
    #this identifies the base century 
    division_result = year // 100
    # if the year is exactly divisible by 100 then the division result represent the century the year is on
    if year % 100 == 0 :
        return division_result
    else: 
        #if its not exactly divisible by 100 it means it is the new century do we divide by 100 and add 1
        return division_result + 1
#==============================================================================================


#==============================================================================================
# You are given two arrays of integers a and b of the same length, and an integer k. We will be iterating through array a from left to right, and simultaneously through array b from right to left, and looking at pairs (x, y), where x is from a and y is from b. Such a pair is called tiny if the concatenation xy is strictly less than k.
# Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.  
a = [1, 2, 3]
b = [1, 2, 3]
k = 31
# i need to access the index because im iterating through a from left to right so from 0 to the len and for b im iterating from -1 to the len? 
def solution(a, b, k):
    #this is to initialize a counter because i need to know how many times something appears
    pairs = 0
    # i use  len(a) because they both have the same lenght so i can just use one
    for i in range(len(a)):
        x= a[i]
        #this part is to be able to loop through the array b from the last index to the first
        y = b[len(b) - 1 - i]
        # i convert them into strings to be able to concatenate instead of adding them and then i convert them in an integer to be able to compare them with k that is also an integer 
        concatenated_num = int(str(x) + str(y))
        if concatenated_num < k:
            pairs += 1
    return pairs
#==============================================================================================


#==============================================================================================
# You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:
# insert x y - insert an object with key x and value y.
# get x - return the value of an object with key x.
# addToKey x - add x to all keys in map.
# addToValue y - add y to all values in map.
# To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).
# Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.
# Example
# For queryType = ["insert", "insert", "addToValue", "addToKey", "get"] and query = [[1, 2], [2, 3], [2], [1], [3]], the output should be solution(queryType, query) = 5.
# The hashmap looks like this after each query:
# 1 query: {1: 2}
# 2 query: {1: 2, 2: 3}
# 3 query: {1: 4, 2: 5}
# 4 query: {2: 4, 3: 5}
# 5 query: answer is 5
# The result of the last get query for 3 is 5 in the resulting hashmap.
queryType = ["insert", "insert", "addToValue", "addToKey", "get"]
query = [[1, 2], [2, 3], [2], [1], [3]]
def solution(queryType, query):
    #i also need to start creating the hasmhmap
    hashmap = {}
    #i have to keep a counter so ill create an empty variable
    sum = 0
    #because the query and the querytype have the same lenght i can just use range on one of them 
    for i in range(len(queryType)):
      if queryType[i] == "insert":
        hashmap[query[i][0]] = query[i][1]
      elif queryType[i] == "addToValue":
          for key in hashmap:
              hashmap[key] += query[i][0]
      elif queryType[i] == "addToKey":
          new_hashmap = {}
          for key in list(hashmap):
              new_key = key + query [i][0]
              new_hashmap[new_key] = hashmap[key]
          hashmap = new_hashmap
      elif queryType[i] == "get":
        if query[i][0] in hashmap:
                sum += hashmap[query[i][0]]
    return sum 
#==============================================================================================


#==============================================================================================
# Given the string, check if it is a palindrome.
# Example
# For inputString = "aabaa", the output should be
# solution(inputString) = true;
# For inputString = "abac", the output should be
# solution(inputString) = false;
# For inputString = "a", the output should be
# solution(inputString) = true.
inputString = "hello"
def solution(inputString):
    reversed_string = inputString[::-1]
    
    if reversed_string == inputString:
        return True
    else:
        return False
#==============================================================================================


#==============================================================================================
# Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.
# Example
# For a = [2, 1, 3, 5, 3, 2], the output should be solution(a) = 3.
# There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.
# For a = [2, 2], the output should be solution(a) = 2;
# For a = [2, 4, 3, 5, 1], the output should be solution(a) = -1.
a = [2, 1, 3, 5, 3, 2]
def solution(a):
    #create an empty set to store the duplicates
    duplicates = set()
    #loop through the array, i dont need the index because in theory the second time that i encounter the duplciate that wil be the second occurence
    for x in a:
        #if the number is in the duplicates then that is the second occurrence of the number 
        if x in duplicates:
            return x
        #but if its not then we add it to the set
        else:
            duplicates.add(x)
        #so for example, the first number 2, is not in the duplicates so it gets added, then the 1 also gets added, then the 3 also gets added, then the 5 also gets added but the 3 is already in the duplicates so it gets returned instead of added
    
    return -1
#==============================================================================================


#==============================================================================================
# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
# Example
# For s = "abacabad", the output should be
# solution(s) = 'c'.
# There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.
# For s = "abacabaabacaba", the output should be
# solution(s) = '_'.
# There are no characters in this string that do not repeat.
def solution(s):
    character_count = {}
    for character in s:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    for character in s:
        if character_count[character] == 1:
            return character
    return "_"
#==============================================================================================


#==============================================================================================
# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
# Example
# For
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# the output should be
# solution(a) =
#     [[7, 4, 1],
#      [8, 5, 2],
#      [9, 6, 3]]
def solution(a):
    #first i loop through the rows
    for i in range(len(a)):
        #then i loop through each element of the row but do it with i + 1 to be careful of the diagonal
        for j in range(i + 1, len(a)):
            #then do the swapping 
            a[i][j], a[j][i] = a[j][i], a[i][j]
    # then reverse it 
    for i in range(len(a)):
        a[i]=a[i][::-1]
    return a  
#==============================================================================================


#============================================================================================== 
# Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.
# Example
# For
# grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
#         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
#         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
#         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
#         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
#         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
#         ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
# the output should be
# solution(grid) = true;
# For grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
#         ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
#         ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
#         ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
#         ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
#         ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
#         ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
#         ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
# the output should be
# solution(grid) = false.
def solution(grid):
    N = len(grid)
    #For each iteration i, two sets are created: row_numbers and col_numbers, to track numbers seen in the i-th row and column, respectively.
    for i in range(N):
        row_numbers = set()
        col_numbers = set()
        for j in range(N):
            #Row Check: For each cell grid[i][j] in row i, if it's not empty and already in row_numbers, return False. Otherwise, add it to row_numbers
            if grid[i][j] != ".":
                if grid[i][j] in row_numbers: 
                    return False
                row_numbers.add(grid[i][j])
            #Column Check: Similarly, for each cell grid[j][i] in column i, check for duplicates and add non-empty numbers to col_numbers.
            if grid[j][i] != ".":
                if grid[j][i] in col_numbers:
                    return False 
                col_numbers.add(grid[j][i])  
    #This loops over the grid in 3x3 blocks, starting at x and y for each sub-grid's top-left corner.           
    for x in range(0, N, 3):
        for y in range(0, N, 3):
            subgrid_numbers = set()
            for i in range(3):
                for j in range(3):
                    num = grid[x+i][y+j]
                    if num != ".":
                        if num in subgrid_numbers:
                            return False
                        subgrid_numbers.add(num)
    return True
#==============================================================================================


#============================================================================================== 
#given an array of integers a. The task is to return another array b where b[i] = a[i - 1] + a[i] + a[i + 1], (if an element does not exist it should be 0)
a = [1,2,3]
#expected result b = [3,4,6]
def sum(a):
    new_arr = []
    for i in range(len(a)):
        current_sum = a[i]
        if i - 1 >= 0:
            current_sum += a[i - 1]
        if i + 1 < len(a):
            current_sum += a[i + 1]
        new_arr.append(current_sum)
    return new_arr
print(sum(a))
#==============================================================================================


#============================================================================================== 
# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
# Example
# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# solution(inputArray) = 21.
# 7 and 3 produce the largest product.
def solution(inputArray):
    #initialized the max product variable by giving it the value of the first comparition of pairs
    max_product = inputArray[0] * inputArray[1]
    #a range loop that starts at 1, ends at the lenght and the minus 1 is so it doesnt go farther than the boundaries of the array
    for x in range(1, len(inputArray) - 1):
        
        product = inputArray[x] * inputArray[x + 1]
        
        if product >= max_product:
            max_product = product
    return max_product
#==============================================================================================


#============================================================================================== 
# After recently joining Instacart's beta testing developer group, you decide to experiment with their new API. You know that the API returns item-specific display-ready strings like 10.0% higher than in-store or 5.0% lower than in-store that inform users when the price of an item is different from the one in-store. But you want to extend this functionality by giving people a better sense of how much more they will be paying for their entire shopping cart.
# Your app lets a user decide the total amount x they are willing to pay via Instacart over in-store prices. This you call their price sensitivity.
# Your job is to determine whether a given customer will be willing to pay for the given items in their cart based on their stated price sensitivity x.
import re
def solution(prices, notes, x):
    total_extra_cost = 0 
    for price, note in zip(prices, notes):
        numbers = re.findall(r'-?\d+\.?\d*', note)
        percentage = float(numbers[0]) if numbers else 0
        if "same as" in note:
            difference = 0 
        elif "higher than" in note:
            in_store_price = price / (1 + percentage / 100)
            difference = price - in_store_price
        elif "lower than" in note:
            in_store_price = price / (1 - percentage / 100)
            difference = price - in_store_price
        total_extra_cost += difference
    if x > 0:
        total_extra_cost = round(total_extra_cost, 2)
    
    return total_extra_cost <= x
#==============================================================================================


#============================================================================================== 
# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
# Example
# For n = 2, the output should be
# solution(n) = 5;
# For n = 3, the output should be
# solution(n) = 13.
def solution(n):
    return n**2 + (n -1)**2
