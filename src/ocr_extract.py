import os


from habanero import Crossref
from pdf2image import convert_from_path
import re

cr = Crossref()


regex = r"(http:\/\/dx.doi.org\/10|10| DOI: 10|DOI:10).\d{4,9}\/[-._;()\/:0-9]+"

if __name__ == '__main__':
    filePath = '../pdfs/test4.pdf'
    doc = convert_from_path(filePath)
    path, fileName = os.path.split(filePath)
    fileBaseName, fileExtension = os.path.splitext(fileName)

    for page_number, page_data in enumerate(doc):
        txt = pytesseract.image_to_string(page_data)
        x = re.sub("\n-", "", txt)

        out = re.search(regex, txt, re.IGNORECASE | re.MULTILINE)
            
        print(x)

        if out is None:
            # If pdf reader fails try ocr?
            print("No Regex Match, Text Dump:\n\n")
            print(out)
            exit(0)

        matches = out.group(0)
        print(matches)

        if page_number == 0:
            break

    # img = convert_from_path('test.pdf')
    # final_text = ""
    # final_text += image_to_string(img)
    # for pg, img in enumerate(images):

    # x = cr.works(ids='10.1177/0018720810374736')
    # x = cr.works(query="Group Influences on Individuals in Organizations")
    # for i, item in enumerate(x['message'][1][0].items()):
    #    print(item)