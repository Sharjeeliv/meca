import os
import time


def search_pdfs(path: str) -> [str]:  # Takes path input and returns a list of names
    pdf_files = []
    for file in os.listdir(path):  # Returns all items in a path
        if file.endswith('.pdf'):
            pdf_files.append(path + "/" + file)
            # print(f"{file} is a pdf")

    return pdf_files


def move_pdf(pdf_path: str):
    try:
        dest = os.getcwd() + "/manual"
        pdf_name = pdf_path.rsplit('/', 1)[1]
        if os.path.exists(dest):
            os.replace(pdf_path, dest + '/' + pdf_name)
        else:
            os.mkdir(dest)
            os.replace(pdf_path, dest + '/' + pdf_name)
    except FileNotFoundError:
        print("Something Not found")


if __name__ == '__main__':
    move_pdf('/Users/sharjeelmustafa/Documents/Development/Python/Projects/zotero_tool/pdfs/Argyris (1960)_theory and '
             'method, understanding OB.pdf')
    pass
