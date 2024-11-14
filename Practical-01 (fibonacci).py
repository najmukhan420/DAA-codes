# Progam of Fibonacci series from 0 t0 10

# TODO: calculate time and space complexity as well you may be required to learn masters theorem

# without recursion (iterative)
def fibo():

    myFib = [0, 1]
    for i in range(1, 10):

        num = myFib[i] + myFib[i - 1]
        myFib.append(num)

    print(myFib)


# with recursion
def rec_fibo(n):
  
    if (n <= 1):
        return n
    
    else: 
        return rec_fibo(n - 1) + rec_fibo(n - 2)

# Driver program

fibo()
n = int(input('Enter a number to find factorial: '))
print(rec_fibo(n - 1 ))

