#Class
from decimal import Decimal #floatの誤差がなくなるClass
d = Decimal(10)   #クラスからオブジェクトを作成 これをインスタンスと呼ぶ
print(d)
print(d+20)
print(d.sqrt()) #Decimalクラスのインスタンスはメソッドも持ってる

#つくってみる
class MyClass:
    pass
i = MyClass()
i.value = 5 #valueというアトリビュートに5を代入
print(i.value)
i2 = MyClass()
i2.value = 10
print(i.value, i2.value) #アトリビュートはインスタンスごとに存在

class MyClass2:
    def __init__(self):
        self.value = 0
        print("This is __init__() method.")
i3 = MyClass2()
print(i3.value)

#角柱を表現しよう
class Prism:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    
    def content(self):
        return self.width * self.height * self.depth

p = Prism(10, 20, 30)
print(p.content())