import os


def search_pdfs(path: str) -> [str]:  # Takes path input and returns a list of names
    pdf_files = []
    for file in os.listdir(path):  # Returns all items in a path
        if file.endswith('.pdf'):
            pdf_files.append(path + "/" + file)
            #print(f"{file} is a pdf")

    return pdf_files
