import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import (
    BASE_DIR,
    DATETIME_FORMAT,
    FILE_NAME,
    RESULTS_DIR
)


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
            self.results_dir / FILE_NAME.format(
                datetime=dt.now().strftime(DATETIME_FORMAT)
            ),
            mode='w',
            encoding='utf-8',
            newline=''
        ) as file:
            csv.writer(file).writerows([
                ('Статус', 'Количество'),
                *(self.status_counts.items()),
                ['Total', sum(self.status_counts.values())]
            ])
