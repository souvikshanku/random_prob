from math import factorial as fact


def f(num):
    digits =list(str(num))
    sum_1 = 0
    for digit in digits:
        sum_1 += fact(int(digit))
    return sum_1
# print(f(342))

def sum_func(inpt):
    digits =list(str(inpt))
    sum_2 = 0
    for digit in digits:
        sum_2 += int(digit)
    return sum_2

# print(sum_func(f(342)))

def g(k):
    flag = False
    num = 1
    while flag == False:
        if sum_func(f(num)) == k:
            flag = True
        else:
            num += 1
    return num

#print(g(3))
#print(sum_func(g(50)))
q = int(input())
n_list = []
m_list = []
for i in range(q):
    n, m = input().split(" ")
    n_list.append(int(n))
    m_list.append(int(m))

#print(n_list, m_list)


for i in range(q):
    sum_ = 0
    for j in range(1, n_list[i]+1):
        sum_ += sum_func(g(j))
    sum_final = sum_ % m_list[i]
    print(sum_final)
