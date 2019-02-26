data = []
count = 0
sum_n = 0
large = []
nice = []
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 200000 == 0:
			print(len(data))
	print("總共有", len(data), "筆資料")


	for n in data:
		sum_n = sum_n + len(n)
	print("平均每筆留言有", sum_n/len(data), "個字")

	for n in data:
		if len(n) > 1000:
			large.append(n)
	print("一共有", len(large), "筆資料自大於1000")	
	#print(large[len(large) - 1])	

	for n in data:
		if "nice, good" in n and len(n) < 100:
			nice.append(n)
	print("一共有", len(nice), "筆資料裡面包含nice & good 資訊")
	print(nice)		
