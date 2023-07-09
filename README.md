# Асинхронный парсер PEP

Парсинг документации Python.

## Описание проекта
Парсер позволяет собирать актуальную информацию документации PEP с помощью фреймворка Scrapy:

- перечень документов PEP ```https://peps.python.org/``` 
- перечень статусов PEP

Данные выводятся в виде **.csv** файла, который сохраняется в директорию ***/results***.

## Используемые технологии
- [Python](https://www.python.org/) 3.8.10
- [Scrapy](https://scrapy.org/) 2.5.1

## Запуск проекта

1. Клонировать репозиторий:
```bash
git clone https://github.com/magicbuka/scrapy_parser_pep.git
```

2. Создать виртуальное окружение:
```bash
python3 -m venv venv
```

3. Активировать виртуальное окружение и установить зависимости из ```requirements.txt```:
```bash
source venv/Scripts/activate
```

```bash
pip install -r requirements.txt
```

4. Запустить парсинг:
```bash
scrapy crawl pep
```


Разработчик проекта [Baranova Anna](https://github.com/magicbuka)