def match(lst):
    dct = {}
    for i in lst:
        if i in dct.keys():
            dct[i] = dct[i]+1
        else:
            dct[i] = 1
    
    pairs = 0
    for k in dct.keys():
        pairs = pairs + int(dct[k]/2)
    
    print(pairs)
lst = list(map(int,input().split()))
match(lst)