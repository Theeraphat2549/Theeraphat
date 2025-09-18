import random

#สุ่มเลขระหว่าง 0 - 9
test_random = random.randint(0, 10)

print("-- gameทายเลข มาเดาใจกันเถอะ --")

#รับค่าการทายเลขจากผู้ใช้
guess_number = int(input("What is your guess number (0-9)?: "))

# condition ==> if-elif-else
if test_random == guess_number:
    print("เก่งมากๆกั้บ งิงิง")

elif guess_number < test_random:
    print("ผิดงับ น้อยไปหน่อย")

elif guess_number > test_random:
    print("ผิดงับ มากไปหน่อย")
