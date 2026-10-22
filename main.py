from logging import config
from pathlib import Path
from utils.statistics import find_max, find_min, calculate_average
from utils.reader import read_numbers
import logging
import json



def main():

    with open("config.json", "r", encoding="utf-8") as file:
        config = json.load(file)
    file_path = config["file_path"]
    log_file = config["log_file"]

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8"
    )

    print("Программа запущена")
    logging.info("Программа запущена")

    def validate_numbers(numbers):
        if len(numbers) == 0:
            raise ValueError("Список измерений пуст")

    print("Текущий рабочий каталог: ", Path.cwd())

    try:
        numbers = read_numbers(file_path)
        logging.info(f"Файл {file_path} прочитан")
        logging.info(f"Файл {file_path} содержит {len(numbers)} значений")
        try:
            validate_numbers(numbers)
        except ValueError as error:
            print("Ошибка данных: ", error)
            logging.error(f"Ошибка валидации: {file_path}")
        print("Содержание файла measurements: ", numbers)
        print("Минимальное: ", find_min(numbers))
        print("Максимальное: ", find_max(numbers))
        print("Среднее: ", calculate_average(numbers))
    except FileNotFoundError:
        print("Файл не найден")
        logging.error(f"Файл {file_path} не найден")
    except ValueError:
        print("Файл содержит некорректные данные")
        logging.error(f"Файл {file_path} содержит некорректные данные")

    logging.info("Программа завершена")

if __name__ == "__main__":
    main()