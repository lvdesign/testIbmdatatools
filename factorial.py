'''
function factorial(n) {
    let result = 1;
    for (n > 1) {
        result *= n;
        n--;
    }
    return result;
}
'''

# While
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n =n-1
    return result



# Recurcive
def factorialNew(n): 
    if (n==1 or n==0):
        return 1
    else:
        # n! = n x (n - 1)!
        return n * factorial(n - 1)

# For
def factorialFor(n):
    num = 1
    for i in range(1, n + 1):
        num = num * i
    return num


print(factorial(5))
print(factorialNew(5))
print(factorialFor(5))