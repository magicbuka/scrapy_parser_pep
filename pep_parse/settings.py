from pathlib import Path

BOT_NAME = 'pep_parse'

PEP_DOMAIN = 'peps.python.org'
ALLOWED_DOMAINS = [PEP_DOMAIN, ]
URLS = [f'https://{PEP_DOMAIN}/']

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = 'results'
FILE_NAME = 'status_summary_{datetime}.csv'

SPIDER_MODULES = [f'{BOT_NAME}.spiders']

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

DATETIME_FORMAT = '%Y-%m-%dT%H-%M-%S'
