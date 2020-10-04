data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line) #去掉換行符號\n
		count += 1
		if count % 1000 == 0: # count是1000的倍數，且餘數為0才印，7%3=1 ,10%6=4 餘數為0才印出
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))

