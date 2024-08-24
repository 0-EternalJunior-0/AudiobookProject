from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from AudiobookProject.parser.royalroad.royalroad.spiders.Royalroad import RoyalroadSpider



# Налаштування проекту Scrapy
settings = get_project_settings()

# Ініціалізуємо процес Crawling
process = CrawlerProcess(settings)

# Додаємо спайд до процесу
process.crawl(RoyalroadSpider)
process.start()