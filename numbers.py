num = 0
x = 0
for i in range (1000):
	if x % 3 == 0:
		num = num + x
	elif x % 5 ==0:
		num = num + x
	x=x+1
print (x)