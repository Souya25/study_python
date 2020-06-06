#論理演算子
v = 65
if  v >= 60 and v <70:
    print("hoge")
if  v >= 60 or v < 40:
    print("hoge")

##素数チェック　for,else
a_num = 43
for num in range(2, a_num):
    if a_num % num == 0:
        print(a_num,"は素数ではありません")
        break
else:
    print(a_num,"は素数です")

#default 引数
def cross(n, m=1):
    m = n * m
    print(m)
cross(10)

#method
bish = ["momoko", "aina", "chicchi", "atsuko", "rinrin", "ayuni"]
print(bish.index("momoko"))
