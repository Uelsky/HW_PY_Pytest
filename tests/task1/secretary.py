import pytest


# Раздел "Функции - использование встроенных и создание собственных"
# Задание «Секретарь»
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
    for i in documents:
        if doc_number == i['number']:
            return i['name']
    return 'Документ не найден'

def get_directory(doc_number):
    for i in directories:
        if doc_number in directories[i]:
            return i
    return 'Полки с таким документом не найдено'

def add(document_type, number, name, shelf_number):
    if shelf_number in directories:
        directories[shelf_number].append(number)
    else:
        directories.update({str(shelf_number): [number]})
    documents.append({'type': document_type,
                      'number': number,
                      'name': name})

add(
    'international passport',
    '311 020203',
    'Александр Пушкин',
    3
)


@pytest.mark.parametrize(
        'doc_number,expected',
        (
            ("10006", "Аристарх Павлов"),
            ("101", "Документ не найден"),
            ("311 020203", "Александр Пушкин")
        )
)
def test_get_name(doc_number, expected):
    result = get_name(doc_number)
    assert result == expected


@pytest.mark.parametrize(
    'doc_number,expected',
    (
        ("11-2", "1"),
        ("311 020203", "3"),
        ("311 020204", "Полки с таким документом не найдено")
    )
)
def test_get_directory(doc_number, expected):
    result = get_directory(doc_number)
    assert result == expected
