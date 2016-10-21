ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens =  ['x', 'y', "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def used_letters(n):
    letter_sum = 0
    for i in range(0,n+1):
        if i < 20:
            letter_sum += len(ones[i])
        if i < 100 and i >= 20:
            letter_sum += len(tens[(i/10)])
            letter_sum += len(ones[i%10])
        if i == 100:
            letter_sum += 10
        if i < 1000 and i > 100:
            
            if i%100 == 0:
                letter_sum += 7 #gets the hundred and part covered
                letter_sum += len(ones[i/100]) #finds how many hundreds it is
                remainder = 900000
            
            else:
                letter_sum += 10 #gets hundred and
                letter_sum += len(ones[i/100]) #finds if it's one, two, three hudnred etc
                remainder = i - (i/100)*100 

            
            if remainder < 20:
                letter_sum += len(ones[remainder])
            
            if remainder < 100 and remainder >= 20:
                letter_sum += len(tens[(remainder/10)])
                letter_sum += len(ones[remainder%10])


        if i == 1000:
            letter_sum += 11
    return letter_sum

print used_letters(1000)

