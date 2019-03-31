num=int(input("Enter number : "))
x=int(num/2)

for i in range(2,x):
	if num%i!=0:
		print("Prime number")

	else:
		print("Not prime numer")
