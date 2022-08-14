import os
import shutil


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
        if os.path.exists(dest):  # Move to Manual search folder
            shutil.copy2(pdf_path, dest + '/' + pdf_name)
        else:  # Create Manual search folder
            os.mkdir(dest)
            shutil.copy2(pdf_path, dest + '/' + pdf_name)
    except FileNotFoundError:
        print("File to move was not found")
