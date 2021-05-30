def function1():
    print("subscribe now")

function2 = function1

function2()


def funcret(num):
    if num==0:
        return print
    if num==1:
        return int

a = funcret(1)
print(a)    