import random
secret_number = random.randint(1,30)

attempts = 0
while True:

    guess = int(input("Taxmini son kiriting>> "))
    attempts += 1
    if guess == secret_number:
        print(f"To'g'ri toptingiz, urinishlar soni {attempts}")
        break
    elif guess < secret_number:
        print("Ko'proq son kiriting ")
    elif guess > secret_number:
        print("Kamroq son kiriting")
    if guess < 1  or guess >30:
        print("Faqat 1 dan 10 gacha bo'lgan sonlarni kiriting")
        continue
