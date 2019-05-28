# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def guess_num(num):
    if num == 2:
        return True
    else:
        return False


# Read a number from the keyboard
num = input("Enter a number between 0 - 10 : ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if guess_num(num):
    print("yes, you right is number 2")
else:
    print("Sorry that's not the number that I have on mind")
