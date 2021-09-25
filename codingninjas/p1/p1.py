L = int(input())
D = int(input())
X = int(input())


ans_arr = []
flag = 0
flag1 = 0

for num in range(L,D):
    arr = [int(i) for i in str(num)]
    if sum(arr) == X:
        arr1 = [str(i) for i in arr]
        ans = ''.join([i for i in arr1])
        ans_arr.append(ans)
        flag = 1
    if flag == 1:
        break

for num in range(D, L-1, -1):
    arr = [int(i) for i in str(num)]
    if sum(arr) == X:
        arr1 = [str(i) for i in arr]
        ans = ''.join([i for i in arr1])
        ans_arr.append(ans)
        flag1 = 1
    if flag1 == 1:
        break







print(ans_arr[0])
print(ans_arr[-1])
