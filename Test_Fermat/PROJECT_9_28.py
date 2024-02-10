import random

def GCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

def Fast_Exponentiation(b , e , m):
 B = b #Base
 result = 1
 M = m #Μodulo
 E = e #exponent
 while (E > 0):
    if ((E % 2) == 1):
        result =(result * B) % M
    E = (E // 2) #Η πραξη // εκτελη και επισρεφει ακεραιο αποτελεσμα ενω η / δεκαδικο.
    B = (B ** 2) % M
 return result


N = 835335 * (pow(2,39014)) - 1

while True:
    a = random.randint(2, N - 1)
    semaphore = False
    if GCD(a, N) > 1 :
        semaphore = True
        print(True)
        break
    if semaphore == False:
        result = Fast_Exponentiation(a,N-1,N)
        if (result == 1):
            print('Probable prime with respect a:n πιθανός πρώτος')
        else :
            print(True)
            break