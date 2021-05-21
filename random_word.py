import wonderwords

amount = int(input("Amount: "))

print(", ".join(wonderwords.RandomWord().word() for x in range(amount))