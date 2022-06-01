# This file is used to test the other functionalities
# It will be replaced with a gui controller
from src.util import search_pdfs
from src.text_extraction import text_extract, ocr_extract
import time
import cProfile


def app():
    start = time.time()
    path = search_pdfs('/Users/sharjeelmustafa/Documents/Development/Python/Projects/zotero_tool/pdfs')

    count = 0
    for pdf in path:
        doi = text_extract(pdf)
        if not doi:
            doi = ocr_extract(pdf)

        if doi:
            count += 1

    print(f"Final DOI Count: {count}")
    end = time.time()
    print(f"Time to complete: {end - start}s")


if __name__ == '__main__':
    cProfile.run('app()')
