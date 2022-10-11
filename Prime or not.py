def prime(num):
    divisors = [2, 3, 5, 7]
    if num in divisors:
        return 'prime'
    else:
        if num%2==0:
            return 'NOT prime, even number'
        else:
            for i in divisors:
                if num%i==0:
                    return 'Not prime'
            else:
                return 'Prime'
while True:
    num = int(input('enter the number to find the prime'))
    print(prime(num))
