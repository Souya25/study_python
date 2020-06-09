#イテレータ
for c, l in enumerate(open('foo.txt')):
    print(l, end='')
    if c == 4:
        break

i = iter([1,2]) #リストをイテレータにする  
print(next(i))  #イテレータから次の要素を得る
print(next(i)) 
print("-----------------------------------------------")

#ジェネレータ
def get_primes(x=2):
    while   True:
        for i in range(2,x):
            if x%i == 0:
                break
        else:
            yield x 
        x += 1

i = get_primes()  #ここでは実行されない
for c in range(10):
    print(next(i)) # ここではじめて実行されている
print("-----------------------------------------------")


##高階関数
def execute(func, arg):
    return func(arg)
print(execute(int,10.0))