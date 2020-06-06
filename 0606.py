
print(5/5**1+9)

print("Earth")
pi = 3.141592653589793238
diameter = 12756.274
print(pi*diameter)

spam = "spamspamspam"
print(spam)
print(spam+"tabetai")
spam+=spam
print(spam)

basho = """ふるいけや
かわずとびこむ
みずのおと"""
print (basho)

day = 24
str_day = str(day)          #型変換
date = str_day+"日"
print(date)

#list
tokyo_temp = [15.1, 15.4, 15.2, 15.4, 17.0, 16.9]
print(tokyo_temp[0])
print(tokyo_temp[0]+ tokyo_temp[1])

#add list
e_tokyo_temp =[100, 100, 100, 100, 100, 100]
tokyo_temp2 = e_tokyo_temp + tokyo_temp
print (tokyo_temp2)

bish = ["momoko", "aina", "chicchi", "atsuko", "rinrin", "ayuni"]

bish[0] = 'gumi'  # list replace
print(bish)

del bish[0]         #list delete
print(bish)

#スライス
print(bish[1:3])
print(bish[:3])
print(bish[1:])