A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Ans = []
for i in A:
	O_i = []
	for x in A:
		O_i.append(i * x)
	Ans.append(O_i)
print(Ans)
