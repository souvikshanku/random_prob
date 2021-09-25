n = int(input())
a = []
b = []
a = [i for i in input().split(" ")]
b = [i for i in input().split(" ")]



flag = 0


for k in range(n):
    if a[k] != b[k] and k<n-1:
        gg = a[k]
        ez = b[k]

        try:
            a_ = int(gg)
            b_ = int(ez)
            if a_ != b_:
                flag = 1
                break
        except:
            for l in range(k+1, n):
                if a[l] == gg and b[l] == ez:
                    pass
                else:
                    flag = 1
                    break
    elif k == n-1:
        flag = 0

if flag == 1:
    print("false")
else:
    print("true")
