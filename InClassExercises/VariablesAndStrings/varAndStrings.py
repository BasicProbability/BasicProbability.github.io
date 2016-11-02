import random

#1 Extract the string "To be Or to take Arms and to sleep No more" and assign it to the variable solution.
# Before doing that, find out how to split a string into a list of words.
hamlet = '''To be, or not to be, that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
And by opposing end them: to die, to sleep
No more; and by a sleep, to say we end
The Heart-ache, and the thousand Natural shocks
That Flesh is heir to? 'Tis a consummation
Devoutly to be wished. To die, to sleep,'''

solution = hamlet.split(" ")


print solution == "To be Or to take Arms and to sleep No more"

#2 The following list of numbers has been jumbled up. Please bring them into their natural order using indexing,
#  slicing and list concatenation.

numbers = [4, 12, 2, 17, 20, 8, 16, 18, 3, 7, 9, 11, 15, 19, 10, 1, 14, 5, 6, 13]
print numbers

#3 Accept any user input and print it back to the user --> check online how to do this

#4 Below we show you how to construct lists and another data structure called a tuple
#  You already know quite a lot about lists, so play around with the list and the tuple
#  and try to figure out how tuples are different from lists.

# 1st way to construct a list
my_list = [1,2,3]
# 2nd way to construct a list
my_list = list([1,2,3])

# 1st way to construct a tuple
my_tuple = (1,2,3)
# 2nd way to construct a tuple
my_tuple = tuple([1,2,3])