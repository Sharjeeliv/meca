import re

import PyPDF2
from habanero import Crossref
from pyzotero import zotero

# Reference for API usage: https://github.com/urschrei/pyzotero
zot = zotero.Zotero(9079397, 'user', 'hLcW1Prkx80idK3qeYB5ev0u')
# Possible have user enter and store in env vars... secret keys?

cr = Crossref()

# primary search is for doi, with doi everything else can be found
# Creating the regex took time, it will take more time to create filters and make it more robust
regex = r"(http:\/\/dx.doi.org\/10|10| DOI: 10|DOI:10).\d{4,9}\/[-._;()\/:0-9]+"

# This part will be dynamic, needs to go through every pdf, common algorithm

testFile = "pdfs/test3.pdf"








with open(testFile, "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    page_0 = reader.getPage(0)
    text = page_0.extractText()
    matches = re.search(regex, str(text), re.IGNORECASE | re.MULTILINE)

    if matches is None:
        # If pdf reader fails try ocr?
        print("No Regex Match, Text Dump:\n\n")
        print(text)
        exit(0)

    matches = matches.group(0)

    # Called the cross ref api to extract text
    doi = matches.strip().split(" ")[1]
    x = cr.works(ids=doi)

    # Index and message the
    # print(x.get('message').keys())

    item = zot.item_template('journalArticle')

    print("Title:", x.get('message').get('title')[0])
    item['title'] = x.get('message').get('title')[0]

    print("Publisher:", x.get('message').get('publisher'))
    # item['publisher'] = x.get('message').get('publisher')

    print("Issue:", x.get('message').get('issue'))
    item['issue'] = x.get('message').get('issue')

    print("Volume:", x.get('message').get('volume'))
    item['volume'] = x.get('message').get('volume')

    print("DOI:", doi)
    item['doi'] = doi

    for i, person in enumerate(x.get('message').get('author')):
        print("Authors:", person.get("given") + " " + person.get("family"))

        item['creators'][0]['firstName'] = person.get("given")
        item['creators'][0]['lastName'] = person.get("family")

        # for types in zot.item_types():
        #     print(types)
        # print(zot.check_items(item))
    resp = zot.create_items([item])
    # print()

    files = [testFile]

    try:
        zot.upload_attachments(
            zot.attachment_simple(files, resp.get('successful').get('0').get('key')))
    except TypeError:
        print("Ignoring TypeError: Because the API uses a string for accessing a list")

    # This works but raises an error because of: TypeError: string indices must be integers

    # if zot.check_items([item]):

    # for field in zot.item_fields():
    #     print(field)
