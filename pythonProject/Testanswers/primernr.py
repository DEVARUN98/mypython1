def sumprime(min,max):
    sum=0
    for a in range(min,max):
        if a>1:
            for i in range(2,a):
                if a%i==0:
                    break

            else:

                sum+=a
    return sum
print(sumprime(1,10))
#print("sum of prime number is ",min,"to ",max," is",sum)