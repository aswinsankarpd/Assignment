def opr(n1,n2,opr):
    dct = {'+':n1+n2,'-':n1-n2,'*':n1*n2,'/':n1/n2}
    print(dct[opr])

n1 = int(input())
n2 = int(input())
op = input()
opr(n1,n2,op)