import requests
import logging

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com').content

page = AllBooksPage(page_content)       # builds page object

books = page.books      #returns the books using the method books from pages.all_books_page

#for book in books:
#    print(book)
logger.debug(f'Found `{page.page_count}` pages.')
for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html'
    logger.debug(f'Trying to connect to `{url}`.')
    page_content = requests.get(url).content
    logger.debug('Creating AllBooksPage from page_content.')
    page = AllBooksPage(page_content)
    books.extend(page.books)