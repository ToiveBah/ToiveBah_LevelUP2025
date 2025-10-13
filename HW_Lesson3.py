#task_1.1
phrase = input("Введите ваше имя: ")
print(f"Привет, {phrase}! Добро пожаловать!")

#task_1.2
quote = input("Введите вашу любимую цитату: ")
author = input("Введите автора цитаты: ")
print(f"\"{quote}\" - {author}")

#task_1.3
word = input("Введите слово: ")
repeat = input("Сколько раз повторить? ")
print(word * int(repeat))

#task_1.4
phrase = input("Введите фразу: ")
print(phrase.upper())
print(phrase.lower())

#task_2.1
width = input("Введите ширину в сантиметрах: ")
height = input("Введите высоту в сантиметрах: ")
square = float(width) * float(height)
print(f"Площадь прямоугольника: {square} кв.см.")

#task_2.2
age = input("Введите ваш возраст в годах: ")
months = int(age) * 12
print(f"Ваш возраст составляет примерно {months} месяцев.")

#task_3.1
age = int(input("Введите ваш возраст: "))
name = input("Введите ваше имя: ")

if age >= 18 and not name == "Иван":
    print("Доступ разрешен!")
elif age < 18:
    print("Доступ запрещен!")
else:   
    print("Доступ запрещен!")