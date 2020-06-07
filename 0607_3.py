#replace
orig_str = "いっぱい"
print(orig_str.replace("い","お"))

#unpack と format 便利

#range
for i in range(10, 21):
    print(i, end=' ')
for i in range(10, 21, 2):
    print(i, end=' ')

#ループカウンタ
seq = [1,2,3,4,5,6]
for cnt in range(len(seq)): #seqを変えるとめんどい
    print(seq[cnt])

for cnt, item in enumerate(seq):  #smart
    print(cnt, item)

#zip
a=[1,2,3,4]
b=[11,12,13,14]
for n,w in zip(a,b):
    print(n,w)

#return
def exchange(n,m):
    m,n = n,m
    return[n,m]
ex = exchange(3,5)
print(ex)
def nexchange(n,m):
    m,n = n,m
    d = 10
    return n,m,d
n,m,d = nexchange(3,5)
print(n,m,d)

#file
f = open("foo.txt", "r", encoding="utf-8")
s = f.read()
print(s)
f.close
