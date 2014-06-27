# Purpose: Pancake Flipping Algorithm
#
# Author: Austin G. Walters
# Date: June 27, 2014
# Python 2.7

# Sorts Pancakes
def sortPancakes(stack):
    
    sorted_index = 10
    for i in reversed(range(len(stack))):
        stack = flip(stack, findLargestPancake(stack, i))
        print("Flip Up", stack)
        stack = flip(stack, i)
        print("Flip Down", stack)
    return stack

        
# All of the pancakes are sorted after index
# Returns the index of largest unsorted pancake
def findLargestPancake(stack, index):
    
    largest_pancake = stack[index]
    largest_index = index;

    for i in range(index):
        if stack[i] > largest_pancake:
            largest_pancake = stack[i]
            largest_index = i

    print ""
    print("Insert Spatula in index", largest_index, "Size", largest_pancake)
    return largest_index

# Slide spatula under pancake at index and flip to top
def flip(stack, index):
    newStack = stack[:(index + 1)]
    newStack.reverse()
    newStack += stack[(index + 1):]
    return newStack


stack = [1, 4, 5, 2, 3, 8, 6, 7, 9, 0]

print"\nUnsorted:"
print stack

print "\nIterating:"
stack = sortPancakes(stack)

print "\nSorted:"
print stack
print ""
