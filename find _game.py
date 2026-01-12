low = 1
high = 30
attempts = 0
print("Bitta son oyla:")
while low <= high:
    guess = (low + high)// 2
    print(f"Men taxmin qilaman: {guess}")
    response = input("Agar oylagan soningiz kattaroq bo'lsa '+',kichik bo'lsa '-', to'g'ri bo'lsa '=' ni bosing>> ")
    attempts += 1

    if response == '+':
        low = guess + 1
    elif response == '-':
        high = guess - 1
    elif response == '=':
        print(f"Topdim! Urinishlar soni: {attempts}")
        break
else:
    print("G'irromlik")
