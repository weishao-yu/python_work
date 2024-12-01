t = int(input())  # input輸入的是字串，所以要轉成整數
w_list = []  # 建立一個空的list
b_list = []

for i in range(t):  # t為要執行的次數 i是0到i-1
    # 先input再split再map轉成整數,split會將數字分開,map會分配給w,b
    w, b = map(int, input().split())
    w_list += [w]
    b_list += [b]

for i in range(t):
    w = w_list[i]
    b = b_list[i]
    sum = w + b
    k = 0
    while k * (k + 1) // 2 < sum:
        k += 1
    if k * (k + 1) // 2 == sum:
        print(k)
    else:
        print(k - 1)
