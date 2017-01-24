from fractions import Fraction
import numpy as np

def simplify(string1, string2):
    intersection = []
    for i in range(0, len(string1)):
        for j in range(0, len(string2)):
            if string1[i] ==  string2[j]:
                intersection.append(string1[i])
    return intersection, len(intersection)

def simplify_string(string1, string2):
    if simplify(string1, string2)[1] == 1:
        simplified1 = string1.replace(simplify(string1,string2)[0][0], "")
        simplified2 = string2.replace(simplify(string1,string2)[0][0], "")
        return [int(simplified1), int(simplified2), float(int(simplified1))/int(simplified2)]

def curious(n,m):
    try:
        if float(n)/m == simplify_string(str(n),str(m))[2]:
            return True
    except:
        return False

def non_trivial():
    non_trivials = []
    simplified = []
    numerators = []
    denominators = []
    for i in range(10,100):
        for j in range(10,100):
            if float(i)/j < 1 and (i%10 != 0 and j%10 != 0):
                if curious(i,j):
                    non_trivials.append(i)
                    non_trivials.append(j)
                    simplified.append(float(i)/j)
                    numerators.append(i)
                    denominators.append(j)
    
    num = np.prod(np.array(numerators))
    denom = np.prod(np.array(denominators))


    return Fraction(num, denom)

if __name__ == '__main__':
    print non_trivial()


    