while True:

	name = input("Ismingizni kiriting (stop ni kiritsangiz dastur tugaydi) >>")
	if name == "stop":
		print("Dastur tugadi")
		break

	elif name.title() == "Admin":
		print("Hush kelebsiz, Admin. Faydalanuvchilar royhatini ko'rasizmi")
	else:
		print("Xush kelibsiz",ism.title())
