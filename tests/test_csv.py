import csv
import os.path

# Задаем уникальный путь к файлу csv
csv_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources/csv_for_test.csv'))


# Создаем файл csv и записываем в него данные
def test_csv():
    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    # Проверяем созданного файла
    assert os.path.exists(csv_file)


# Проверка csv
def test_read_csv():
    with open(csv_file) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            assert len(row) == 3

    # Удаляем файл csv
    os.remove(csv_file)