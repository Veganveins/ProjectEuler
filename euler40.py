start = "1"
for i in range(2,1000000):
    start = start + str(i)
print int(start[0])* int(start[9])* int(start[99]) * int(start[999]) * int(start[9999]) * int(start[99999]) * int(start[999999])