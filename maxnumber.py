def max_num(a):
    if len(a)==1:
        return a[0]
    else:
        for i in a:
            a[i]>a[i+1]
        return a[i]


a=[2, 4, 10, [12, 4, [100, 99], 4], [3, 2, 99], 0]
result=max_num(a)