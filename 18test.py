n1 = [75]
n2 = [95,64]
n3 = [17, 47, 82]
n4 = [18, 35, 87, 10]
n5 = [20, 4, 82, 47, 65]
n6 = [19, 1, 23, 75, 3, 34]
n7 = [88, 2, 77, 73, 7, 63, 67]
n8 = [99, 65, 4, 28, 6, 16, 70, 92]
n9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
n10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
n11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
n12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
n13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
n14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
n15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

triangle = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15]
    
while len(triangle) > 1:
    row = len(triangle)
    subject = triangle[row - 2]  
    add = triangle[row - 1]
    for i in range(0, len(subject)):
        subject[i] += max(add[i], add[i+1])  
    
    triangle[row - 2] = subject
    triangle.pop()

print triangle
    
    
        
    


        
