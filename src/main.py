# This file is used to test the other functionalities
# It will be replaced with a gui controller
from src.utils import search_pdfs, move_pdf
from src.text_extraction import text_extract, ocr_extract
from src.data_verification import get_crossref_work
import time
import concurrent.futures
from zotero_entry import create_zotero_entry


def extract_doi_from_pdf(pdf):
    doi = text_extract(pdf)
    if not doi:
        doi = ocr_extract(pdf)
    return doi, pdf


def doi_extraction(pdfs):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(extract_doi_from_pdf, pdfs)
        return results


def filter_extractions(pdf_data):
    doi, pdf_path = pdf_data
    if doi is not None:
        return True
    else:
        move_pdf(pdf_path)
        return False


def app():
    start = time.time()
    pdfs = search_pdfs('/Users/sharjeelmustafa/Documents/03 Projects/Development/zotero_tool/pdfs')

    pdfs_data = filter(lambda result: filter_extractions(result), doi_extraction(pdfs))
    pdfs_metadata = [get_crossref_work(pdf_data) for pdf_data in pdfs_data]  # Iterator object
    [create_zotero_entry(pdf_metadata) for pdf_metadata in pdfs_metadata]

    end = time.time()
    print(f"Time to complete: {round(end - start, 2)}s")


if __name__ == '__main__':
    app()
