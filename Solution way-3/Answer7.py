# question 7

def longest_cons(x):
    long_stk = 0

    for i in x:
        present_number = i
        present_stk = 1

        while present_number + 1 in x:
            present_number += 1
            present_stk += 1

        long_stk = max(long_stk, present_stk)

    return long_stk

given_arr = [100,4,200,1,3,2]        #can take input from usear also


print(longest_cons(given_arr))

