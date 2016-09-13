n = 0
while n <= 100: 
    if (n % 3 == 0) and (n % 5 == 0):
    	print "Fizz Buzz"
    if n % 3 == 0:
        print "fizz"
    if n % 5==0:
    	print "buzz"
    else:
    	print str(n)
    n=n+1

   