balance = 0.0

while True:
    print("\n--- Bank hisabi ---")
    print("1- Balansni ko'rish")
    print("2- pul qo'chishi")
    print("3- pul yechish")
    print("4- Dasturdan chiqish")

    tanlov = int(input("\nTonlavingizni kiriting>> "))

    if tanlov == 1:
	    print(f"Sizning balansingiz {balance}")

    elif tanlov == 2:
	    miqdor = float(input("Qo'shiladigan summani kiriting>> "))
	    balance = balance + miqdor
	    print(f"\nHisobingizga {miqdor} qo'shildi")
	    print(f"Hozirgi balansingiz {balance}")

    elif tanlov == 3:
	    miqdor = float(input("Yechiladigan summani kiriting>> "))
	    if miqdor > 0 and miqdor <= balance:
	        balance = balance - miqdor 
	        print(f"\nHisobingizdan {miqdor} pul yechildi")
	        print(f"Hisobingizda {balance} qo'ldi")
	    else:
	    	print("Hisobingizda mablag' yetarli emas")
	    	print(f"Balansingiz {balance}")

    elif tanlov ==4:
	    print("Dastur tugadi")
	    break
    else:
	    print("Xoto faqat 1 dan 4 gacha bo'lagan sonlar")

