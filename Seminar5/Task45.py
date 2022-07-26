# 5. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


Mylist = [1, 2, 4, 5 ,6, 8, 9, 10]
def lists(Mylist ):
    Mylist1 = set(Mylist)
    temp_list = set(list(range(Mylist[0], Mylist[-1]+1)))
    res = temp_list - Mylist1 
    return res
print(lists(Mylist ))


def Mylists(a):
    step = []
    for i in range(1, len(a)-1): # Len(A)-1 фактически является индексом последнего элемента в списке
        if a[i+1] - a[i] > 1:
            step.append(a[i] + 1)
    return step
print(Mylists(Mylist))
