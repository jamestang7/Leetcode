def lps(s):
    n = len(s)
    def Pal(str1):
        if len(str1) == 0 or len(str1) == 1:
            return True
        elif str1[0] == str1[-1]:
            return Pal(str1[1:-1])
        else:
            return False 

    # Create a table to store results of subproblems
    L = [[(0,(0,0)) for x in range(n)] for x in range(n)]
 
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = (1,(0,0))

    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if s[i] == s[j] and cl == 2:
                L[i][j] = (2, (i, j))
                
            elif s[i] == s[j]:
                a = L[i + 1][j]
                b = L[i][j - 1]
                c = L[i+1][j-1]
                num_list = [i[0] for i in (a, b, c)]
                cor_list = [i[1] for i in (a, b, c)]
                map = dict(zip(num_list, cor_list))
                if Pal(s[i: j + 1]):
                    L[i][j] = (c[0] + 2, (i, j))
                else:
                    L[i][j] = (max(map.keys()), map[max(map.keys())])
                
            else:
                a = L[i+1][j]
                b = L[i][j-1]
                if a[0] > b[0]:
                    L[i][j] = (a[0], a[1])
                else:
                    L[i][j] = (b[0], b[1])
            print(i,j, L[i][j])
        print("------------")
    length = L[0][n-1][0]
    i, j = L[0][n-1][1]

    sub = s[i: j + 1]
    return sub

# Driver program to test above functions
seq = "aacabdkacaa"
print(lps(seq))

