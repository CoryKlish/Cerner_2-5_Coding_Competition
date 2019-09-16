#cerner_2^5_2019

import random

def thanos_sort():
    if not i_am_inevitable():
        print(myList)
        
    while i_am_inevitable():
        print('Eliminating half of list...')
        snap_finger()
        print('Remaining: ', myList, '\n')

def snap_finger():
    for i in range(int(len(myList) / 2)):
        undying = random.randint(0, len(myList) - 1)
        myList.pop(undying)
    
def i_am_inevitable():
    if (myList == sorted(myList)):
        return False
    else:
        return True

input_list = input('Enter the list to sort delimited by space: ').split()
myList = list(map(int, input_list))
thanos_sort()
