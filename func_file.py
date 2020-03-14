#cycle parts of key
def cycle_parts(l, ti):
    if (ti == 1):
        tmp = l[0]
        l.pop(0)
        l.append(tmp)
        return l
    return cycle_parts(cycle_parts(l, 1), ti - 1)
# 6 3 7 4 8 5 10 9
def key_replace(p):
    k = [p[5], p[2], p[6], p[3], p[7], p[4], p[9], p[8]]
    return k

def m_replace(m):
#2 6 3 1 4 8 5 7
    m = [m[1], m[5], m[2], m[0], m[3], m[7], m[4], m[6]]
    return m
def m_rereplace(m):
#4 1 3 5 7 2 8 6
    m = [m[3], m[0], m[2], m[4], m[6], m[1], m[7], m[5]]
    return m

#change 4 bits, return = 8 bits
def ext_4(p):
# 4 1 2 3 2 3 4 1
    p = [p[3], p[0], p[1], p[2], p[1], p[2], p[3], p[0]]
    return p

#s0 manipulation
def replace_s0(row1, row2, col1, col2):
#    0 1 2 3
# 0| 1 0 3 2
# 1| 3 2 1 0
# 2| 0 2 1 3
# 3| 3 1 0 2
    s0 = [[1, 0, 3, 2],
          [3, 2, 1, 0],
          [0, 2, 1, 3],
          [3, 1, 0, 2]]
#find out a row
    row = str(row1)+str(row2)
    row = int(row, 2)
#findout a col
    col = str(col1)+str(col2)
    col = int(col, 2)
    if(s0[row][col] == 0):
         res = format(s0[row][col], "b") + format(s0[row][col], "b")
    elif(s0[row][col] == 1):
        res = '0' + format(s0[row][col], "b")
    else:
        res = format(s0[row][col], "b")

    return res


#s1 manipulation
def replace_s1(row1, row2, col1, col2):
#    0 1 2 3
# 0| 1 1 2 3
# 1| 2 0 1 3
# 2| 3 0 1 0
# 3| 2 1 0 3
    s0 = [[1, 1, 2, 3],
          [2, 0, 1, 3],
          [3, 0, 1, 0],
          [2, 1, 0, 3]]

#find out a row
    row = str(row1)+str(row2)
    row = int(row, 2)

#findout a col
    col = str(col1)+str(col2)
    col = int(col, 2)

    if(s0[row][col] == 0):
         res = format(s0[row][col], "b") + format(s0[row][col], "b")
    elif(s0[row][col] == 1):
        res = '0' + format(s0[row][col], "b")
    else:
        res = format(s0[row][col], "b")

    return res

#replace 4 bits after s0 s1 manipulation
def replace_4(x):
#2 4 3 1
    x = [x[1],x[3],x[2],x[0]]
    return x

def round(r, k):
    #XOR with key
    for i in range(len(r)):
        r[i] = (r[i] + k[i]) % 2

        #make s0 = return 2 bits and s1 = return 2 bits replace
    r = replace_s0(r[0], r[3], r[1], r[2]) + replace_s1(r[4], r[7], r[5], r[6])
    #final switching inside r(4 bits)
    r = replace_4(r)
    
    for i in range(len(r)):
        r[i] = int(r[i])
    return r
