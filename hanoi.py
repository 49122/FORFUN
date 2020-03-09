def move(a,b):
    print("mueve el disco de {}  a  {}".format(a,b))

def hanoi(n,a,b,c):
    if n==0 :
        pass
    else:
        hanoi(n-1,a,c,b)
        move(a,c)
        hanoi(n-1,b,a,c)

hanoi(4,"A","B","C")
X=input()
