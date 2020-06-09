#lambda
data = [(14,312,32),(23, 2 ,31),(31,312,312)]
data.sort(key=lambda val: sum(val), reverse = True)
print(data)

# リスト内包表記
height_data = [311,321,351,294,300]
total =sum(height_data)
length = len(height_data)
mean =total/length
variance = sum([(height-mean)**2 for height in height_data])/length
print(variance)
