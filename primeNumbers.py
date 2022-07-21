# Prime numbers can only be devided by itself and 1
# We are looking for all the prime number in the chosen number

my_num = input('choose a number: ')
my_num = int(my_num)+1
primes = []
for i in range(1, my_num):
    if i > 1:
        for a in range(2, i):
            if (i % a) == 0:
                break
        else:
            primes.append(i)
print('All the primes in ', my_num - 1, 'are ', primes)
exit()
