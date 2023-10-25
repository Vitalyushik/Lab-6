import numpy as np
while True:
    try:
        cr_num = int(input("Введите кол-во критериев: "))
        break
    except ValueError:
        print('Ошибка ввода, введите кол-во критериев цифрой')
s_matr = np.eye(cr_num)
a = 1   
for i in range(a, cr_num+1):
    for j in range(a+1, cr_num+1):
        while True:
            try:
                s_matr[i-1][j-1] = round(float(input('Введите сравнение К{0}-К{1}:'.format(i, j))),3)
                break
            except ValueError:
                print('Ошибка ввода, введите значение цифрой')
        s_matr[j-1][i-1] = round(s_matr[i-1][j-1]**(-1), 2)
    a += 1
comp_list = [round(sum(i),2) for i in s_matr]
out_list = [round(i/sum(comp_list), 2) for i in comp_list]
if (sum(out_list)) != 1.0:
    index = out_list.index(max(out_list))
    k = (sum(out_list)) - 1.0
    out_list[index] -= k
print('Весовые коэффициенты')
for i in out_list:
    print(i, end=' ')

