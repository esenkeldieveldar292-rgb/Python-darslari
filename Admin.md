while True:

	ism = input("Ismingizni kiriting (stop ni kiritsangiz dastur tugaydi) >>")
	if ism == "stop":
		print("Dastur tugadi")
		break

	elif ism.title() == "Admin":
		print("Hush kelebsiz, Admin. Faydalanuvchilar royhatini ko'rasizmi")
	else:
		print("Xush kelibsiz",ism.title())
