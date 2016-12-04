workfile = open("names", "r")
lines = workfile.read().split(',')

# clean up formatting:
for i in range(0, len(lines)):
    lines[i] = lines[i].lstrip() 
    lines[i] = lines[i].rstrip() 

#create an alphabetized list of all the unique names
lines = sorted(lines)
blank = [0]
lines = blank + lines

#store the alphabetical position of each name
name_rank = list(range(1,5164))

#store the alphabetical value for each name
alphabetical_value = []
letters = ['"', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(1, len(lines)):
    value = 0
    for j in range(1, len(lines[i])):
        letter = lines[i][j]
        value += letters.index(letter) 
    alphabetical_value.append(value)  

alphabetical_value = blank + alphabetical_value
name_score = [0]

for i in range(1, len(lines)):
    name_score.append(alphabetical_value[i]*i)

print sum(name_score)












