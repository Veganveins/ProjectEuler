"""
How many ways are there to make $2 with any number of coins, if you can choose from :

.01, .02, .05, .1, .2, .5, $1, $2 ?


****1 way using a $2 coin.
****1 way using 2 $1 coins
****1 way using 4 50 cent
****1 way using 10 20 cent
****1 way using 20 10 cent
****1 way using 40 5 cent
****1 way using 100 2 cent
****1 way using 200 1 cent 


How many ways using at least 1 dollar?  ----> 2

How many ways using at least 1 50 cent?  -----> 4

How many ways using at least 1 20 cent?  -----> 10

How many ways using at least 1 10 cent?  -----> 

How many ways using at least 1 5 cent?    ----> ?

How many ways using at least 1 2 cent?    ---> 100

****1 way using 200 1 cent coins
"""

def find_ways_with_five_cents():
    a = 0
    b = 0
    c = 0
    ways = 0
    for i in range(0,41):
        a = i
        for j in range(0, 100):
            b = j
        for k in range(0,200):
            c = k
            if (.05*a + .02*b + .01*c) == 2:
                print .05*a + .02*b + .01*c
                ways += 1

    return ways





if __name__ == "__main__": 
    print find_ways_with_five_cents()