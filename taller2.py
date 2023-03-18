a = {6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
b = {0,2,4,6,8,10,12,14,16,18,20,22,24}
c = {1,4,8,10,12,15,18,20}
d = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43}

def union(a, b):
     u = a|b
     return u
def inter(a, b):
    i = a&b
    return i
def dife(a, b):
    i = a-b
    return i
def dife_sime(a,b):
    d = a^b
    return d

op1 = inter(b, dife_sime(c, d))
print(op1)

op2 = union(inter(a,c), b)
print(op2)

op3 = dife(union(b,d),c)
print(op3)

op4 = dife_sime(dife(a,b), inter(a,d))
print(op4)
