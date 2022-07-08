from operator import truediv
playerA = None
playerB = None
num = 0

for i in range (31):
    print('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능 :')
    while True:
        a = int(input())
        if type(a) == int:
            break
        else:
            print('정수를 입력하세요')
    while True:
        if a == 1 or a == 2 or a ==3:
            break
        else:
            print('1,2,3 중 하나를 입력하세요')
            a = int(input())
    for j in range(0,a):
        num += 1
        if i % 2 == 0:
            print('playerA :', num)
        else:
            print('playerB :', num)
        if num == 31:
            break
    if num == 31:
        if i % 2 == 0:
            print('playerA 승리')
            break
        else:
            print('playerB 승리')
            break 
    
