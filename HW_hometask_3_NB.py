# task_1_Line slices
text = "Питон — это круто!"

print(text[:6])
print(text[:-2])
print(text[::-1])
print(text[::2])


# task_2_Filtering a list by index
numbers = [10, 25, 30, 45, 50, 65, 70]
new_numbers = numbers[::2]

print(new_numbers)


# task_3_Replacing list items
shopping = ["молоко", "хлеб", "сыр", "яблоки"]

shopping[1] = "батон"
del shopping[2]
shopping.append("йогурт")

print(shopping)


# task_4_Combining lists
a = [1, 3, 5]
b = [2, 4, 6]

new_list = a + b
new_list.reverse()
len([new_list])

print(new_list)


# task_5_Remove all duplicates
data = [1, 2, 2, 3, 4, 4, 5, 1]

new_data = set(data)
data = list(new_data)

print(data)


# task_6_Working with a dictionary of countries
countries = {
    "Россия": "Москва",
    "Италия": "Рим",
    "Испания": "Мадрид"
}

countries["Германия"] = "Берлин"
countries["Испания"] = "Барселона"
print(countries)

for country in countries:
    print(f"Столица {countries[country]} находится в стране {country}")


# task_7_Counting letters
word = "программирование"
vowels = {"а", "о", "у", "ы", "э", "я", "ю", "ё", "и", "е"}

letters = set(word)
letters_num = len(letters)
letters_intersection = vowels.intersection(letters)

print(letters)
print(letters_num)
print(letters_intersection)

# task_8_Reverse dictionary
countries_and_capitals = {"Россия": "Москва", "Франция": "Париж", "Япония": "Токио"}

new_countries_and_capitals = {capital: country for country, capital in countries_and_capitals.items()}
  
print(new_countries_and_capitals)


# task_9_List of films
list_of_films = ["Звездные воины", "Властелин колец", "Чем мы заняты в тени", "Горец", "Зеленая миля"]

list_of_films.sort()
list_of_films.insert(0, "Интерстеллар")
list_of_films.pop()

print(list_of_films)


# task_10_Parsing a number list
nums = [15, 2, 30, 4, 50, 6, 75, 8]

nums_min = min(nums)
nums_max = max(nums)
nums_middle = sum(nums) / len(nums)

print(nums_min, nums_max, nums_middle)

for i in nums:
    if i > nums_middle:
        nums.remove(i)

nums.sort()

print(nums)


