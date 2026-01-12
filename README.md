while True:
	age = int(input("Yoshingizni kiriting>>"))
	if age ==0:
		print("Dostur tugadi")
		break
	elif age <= 3:
		price = 0
	elif age <= 10:
		price = 2000
	elif age <=18:
		price = 5000
	elif age <=35:
		price = 7000
	elif age <= 65:
		price =10000
	elif age >=66:
		price = 4000
	print(f" Sizning yol kirangiz {price} ")
