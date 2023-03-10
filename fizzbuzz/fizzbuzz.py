#Fizzbuzz: if number is divisible by 3, print "Fizz", if number is divisible by 5, print "Buzz", if number is divisible by 3 & 5, print "FizzBuzz"

numbers = range (1, 100)

for i in numbers:
       if i%3 == 0:
           print ("fizz")
       if i%5 == 0:
           print ("buzz")
       if i%5 == 0 and i%3 == 0:
           print ("fizzbuzz")
       else:
          print (i)