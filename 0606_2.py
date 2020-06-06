#2d
city_temp = [
    [14, 31, 31, 31],
    [43, 53, 61, 13],
    [65, 13, 31, 13]
    ]
print(city_temp[1])
print(city_temp[2][1]- city_temp[1][3])

#sum,max,min,len
print(sum(city_temp[0]))
print(max(city_temp[0]))
print(min(city_temp[0]))
print(len(city_temp[0]))

#for
bish = ["momoko", "aina", "chicchi", "atsuko", "rinrin", "ayuni"]
print(bish)
for i in bish:
    print(i)

#practice_variance
monk_fish_team  = [158, 157, 163, 157, 145]

total = sum(monk_fish_team)
length = len(monk_fish_team)
mean = total/length
variance = 0
for data in monk_fish_team:
    variance += (data-mean)**2
variance /= length
print(variance)

#range
for cnt in range(10):
    print(cnt)
for cnt in range(5,10):
    print(cnt)

#if
if 4+4 == 16 :
    print("4+4 = 16")
if 4 < len([1, 4, 2]):
    print("2true")
if "うんこ" == "うんこ":
    print("unko")
if "unkounkounkounko" in "oun":
    print("oun")
if "ounk" in "unkounkounkounko" :
    print("ounk")

#else、elif
if 4+4 == 16 :
    print("4+4 = 16")
else:
    print("4+4 !=  16")
if 4+4 == 16 :
    print("4+4 = 16")
elif 4+4 ==8:
    print("4+4 = 8")

#kansuu rei abs()
print(abs(-19312))
from random import randint

#kansuu
def bish_osi():
    bish = ["momoko", "aina", "chicchi", "atsuko", "rinrin", "ayuni"]
    osi = bish[randint(0,5)]
    print(osi)
bish_osi()

def return_osi():
    bish = ["momoko", "aina", "chicchi", "atsuko", "rinrin", "ayuni"]
    osi = bish[randint(0,5)]
    return osi
my_osi = return_osi()
print ("私の推しは", my_osi,"です。")
