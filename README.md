# scrapy_parser_pep

Склонируйте проект:
```bash
git clone git@github.com:ViaDo1orosa/scrapy_parser_pep.git
```
Создайте и активируйте виртуальное окружение:
##### Windows:
```bash
python -m venv venv
source venv/Scripts/activate
```
##### Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
Установите зависимости командой:
```
pip install -r requirements.txt
```
## Запуск парсера:
```bash
scrapy crawl pep
```
После запуска парсера будет создано 2 файла с результатами работы в директории `pep_parse/results/`:

1. pep_ДатаВремя.csv - «Номер», «Название» и «Статус»
2. status_summary_ДатаВремя.csv - «Статус», «Количество» и «Общее число документов»

## Технологии
- [Python](https://www.python.org/)
- [Scrapy](https://pypi.org/project/Scrapy/)

## Автор: 
[Даниил Варлащенко](https://github.com/ViaDo1orosa)
***
