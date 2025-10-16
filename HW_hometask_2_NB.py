# task_1_Checking the greeting
text = input("Введите фразу: ")

if "привет" in text.lower():
    input("И тебе привет!")

elif "пока" in text.lower():
    input("Уже уходишь?")

else:
    input("Ты молчалив сегодня...")


# task_2_Table of powers
n = int(input("Введите количество чисел: "))

for i in range(1, n + 1):  
    print(f"{i}, {i}^{2} = {i ** 2}, {i}^{3} = {i ** 3}")


# task_3_Secret number
saved_guess = 7
guess = int(input("Введите задуманное число: "))
while True:
    if guess < 7:
        print("Мало!")
    elif guess > 7:
        print("Много!")
    else:
        print("Верно!")
    break


# task_4_Vowels in Focus
text = input("Введите текст: ")
list_of_vowels = "аеёиоуыэюя"

for i, letter in enumerate(text):
    if letter in list_of_vowels:
        print(i, letter) 


# task_5_Frogs in the swamp
for frog in range(1, 4):
    for hummock in range(1, 4):
        if frog == hummock:
            continue
        else:
            print(f"лягушка {frog} прыгает на кочку {hummock}")
