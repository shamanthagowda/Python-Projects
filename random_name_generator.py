import random
import re
# creating list of first_name and last_name
first_name=['apple','ball','cat','dog']
second_name=['123','345','236842','21873','834287','27342']


def rand_number(first, second):
    # generating random index numbers for first name and second name
    def first_rand_num(first):
        rand_1=random.randint(0,first-1)
        return first_name[rand_1]
    def second_rand_num(second):
        rand_2=random.randint(0,second-1)
        return second_name[rand_2]
    print(first_rand_num(first)+' '+second_rand_num(second))


# calling the function
name=rand_number(len(first_name),len(second_name))

# Asking if the user need to try once again
trial=True
while trial:
    acceptance = input('enter y to continue or q to quit')
    acceptance=acceptance.lower()
    if acceptance in ['y','yes']:
        rand_number(len(first_name), len(second_name))
    else:
        trial=False
else:
    print('Thankyou..!!')