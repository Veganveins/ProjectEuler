def sunday(n):
    #first sunday is on the 7th Jan 1 1990
    #net = 1 starts on Tuesday Jan 1 1901
    #i think there may be an issue still because this may be "accidentally correct"
    #this might be the number of tuesdays that fall on the first of the month
    month = 1
    year = 1901
    count = 0
    net = 1

    for year in range(year,n):
        for month in range(1,13):
            if month in [1,3,5,7,8,10, 12]:
                net += 31
                if net%7 == 0:
                    count += 1
            elif month in [4, 6, 9, 11]:
                net += 30
                if net%7 == 0:
                    count += 1
            elif month == 2:
                if year%4 != 0:
                    net += 28
                    if net%7 == 0:
                        count += 1
                elif year%4 == 0 and year%100 != 0:
                    net += 28
                    if net%7 == 0:
                        count += 1
                elif year%400 != 0:
                    net += 28
                    if net%7 == 0:
                        count += 1
                elif year%400 == 0:
                    net += 29
                    if net%7 == 0:
                        count += 1

    return count, net, net%7
        
      
            # if month in [1, 3, 5, 7, 8, 10]:
            #         net += 31
            #         month += 1

            # elif month in [4, 6, 9, 11]:
            #     net += 30
            #     month += 1  

            # elif month == 2:
            #     if year%4 == 0 and year%100 == 0:
            #         net += 29
            #         month += 1
            #     elif year%4 and year%400 == 0:
            #         net += 29
            #         month += 1
            #     elif year%4 !=0 or year%400 !=0:
            #         net += 28
            #         month += 1  

            # elif month == 12:
            #         net += 31
            #         year += 1
            #         month = 1


    #return count


print sunday(2001)


