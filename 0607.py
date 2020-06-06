#module, import, as, from,-------------------------
import random as rd
from statistics import median

print(rd.random())

monk_fish_team = [231, 321,  312, 33]
print(median(monk_fish_team))


#dictionary-----------------------------------------
people = {"ニックネーム":"れにちゃん",
          "出身地": "神奈川県",
          "キャッチフレーズ":"感電少女"}
print(people["出身地"])
print(people)

people["キャッチフレーズ"] = "鋼の錬金術師" #一部要素変更
print(people)

people["生年月日"] = "19930621" #要素追加
print(people)

del people["ニックネーム"]  #キーの削除
print(people)

if "生年月日" in people:    #キーの検索
    print(people["生年月日"]) 

for key in people:
    print(key, people[key])


#set----------------------------------
dice = {1, 2, 3, 4, 5, 6}
#和集合
prime = {2, 3, 5, 7, 11, 13}
fib = {1, 1, 2, 3, 5, 8, 13}
prime_fib = prime | fib
print(fib)              #重複してないのが確認
print(prime_fib)        #和集合
#差集合
even = {2, 4, 6, 8, 10}
odd_dice = dice - even
print(odd_dice)
#交わり
even_dice = dice & even
print(even_dice)   #その補集合の対象差もあるよ
#list to set
number = [1,3,54,5,42,3,1,23,3,1,4]
s_number = set(number)
print(s_number)

#タプル------------------------------
month_names = ("January", "February")
month_names += ("March", "April")  # add tuple
print(month_names)

pref_capitals = {(43,141):"hokkaido",
                 (40,140):"aomori",
                 (39,141):"iwate"}
print(pref_capitals[(40,140)])

