from pathlib import Path

def read_numbers(file_path):
    numbers = []
    with open(file_path, "r", encoding="utf-8") as file: #открытие и преобразование файла
        for line in file: #Пока line в файле
            numbers.append(float(line))
        return numbers

