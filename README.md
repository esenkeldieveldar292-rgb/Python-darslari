while True:
	yosh = int(input("Yoshingizni kiriting>>"))
	if yosh ==0:
		print("Dostur tugadi")
		break
	elif yosh <= 3:
		price = 0
	elif yosh <= 10:
		price = 2000
	elif yosh <=18:
		price = 5000
	elif yosh <=35:
		price = 7000
	elif yosh <= 65:
		price =10000
	elif yosh >=66:
		price = 4000
	print(f" Sizning yol kirangiz {price} ")