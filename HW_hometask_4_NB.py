# task_1_Line slices
def line_slices(text):
    return text[:6], text[:-2], text[::-1], text[::2]

text = "Питон — это круто!"
print(line_slices(text))



# task_2_Filtering a list by index
def list_by_index(numbers):
    new_numbers = numbers[::2]
    return new_numbers

numbers = [10, 25, 30, 45, 50, 65, 70]
print(list_by_index(numbers))



# task_3_Replacing list items
def list_items(shopping):
    shopping[1] = "батон"
    del shopping[2]
    shopping.append("йогурт")
    return shopping
    
shopping = ["молоко", "хлеб", "сыр", "яблоки"]
print(list_items(shopping))



# task_4_Combining lists
def combining_list(a, b):
    new_list = a + b
    new_list.reverse()
    print(len(new_list))
    return new_list

a = [1, 3, 5]
b = [2, 4, 6]
print(combining_list(a, b))



# task_5_Remove all duplicates
def all_dublicates(data):
    new_data = set(data)
    data = list(new_data)
    return data

data = [1, 2, 2, 3, 4, 4, 5, 1]
print(all_dublicates(data))



# task_6_Working with a dictionary of countries
def dictionary_of_countries(countries):
    countries["Германия"] = "Берлин"
    countries["Испания"] = "Барселона"
    print(countries)

    for country in countries:
         print(f"Столица {countries[country]} находится в стране {country}")

    return countries

countries = {
    "Россия": "Москва",
    "Италия": "Рим",
    "Испания": "Мадрид"
    }
print(dictionary_of_countries(countries))



# task_7_Counting letters
def counting_letters(word, vowels):
    letters = set(word)
    print(letters)
    letters_num = len(letters)
    print(letters_num)
    letters_intersection = vowels.intersection(letters)
    print(letters_intersection)
    return letters, letters_num, letters_intersection

word = "программирование"
vowels = {"а", "о", "у", "ы", "э", "я", "ю", "ё", "и", "е"}
print(counting_letters(word, vowels))



# task_8_Reverse dictionary
def reverse_dictionary(countries_and_capitals):
    new_countries_and_capitals = {capital: country for country, capital in countries_and_capitals.items()}
    return new_countries_and_capitals

countries_and_capitals = {"Россия": "Москва", "Франция": "Париж", "Япония": "Токио"}  
print(reverse_dictionary(countries_and_capitals))



# task_9_List of films
def films(list_of_films):
    list_of_films.sort()
    list_of_films.insert(0, "Интерстеллар")
    list_of_films.pop()
    return list_of_films

list_of_films = ["Звездные воины", "Властелин колец", "Чем мы заняты в тени", "Горец", "Зеленая миля"]
print(films(list_of_films))



# task_10_Parsing a number list
def parsing_a_number_list(nums):
    nums_min = min(nums)
    nums_max = max(nums)
    nums_middle = sum(nums) // len(nums)

    print(nums_min, nums_max, nums_middle)

    for i in nums:
        if i > nums_middle:
            nums.remove(i)

    nums.sort()
    return nums

nums = [15, 2, 30, 4, 50, 6, 75, 8]
print(parsing_a_number_list(nums))


