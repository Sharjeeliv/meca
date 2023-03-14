Zotero Metadata Extraction and Citation Automation (MECA)
---
<p>
Zotero-MECA is a tool to automate the steps of manually moving local PDFs 
to a zotero database. The application will do the following:
</p>

1. Extract the DOI from the PDF
2. Fetch verified metadata for the PDF from CrossRef 
3. Format the metadata in accordance to APA style
4. Package the metadata and file 
5. Upload the package to Zotero
6. Failed PDFs are flagged and move to a folder for manual review.

### Application Structure

<p>
The application is developed in python using a layered architecture for 
maintainability and extensibility. It consists of text extraction, data verification, text processing, and zotero entry as layers.
</p>

`Text Extraction`
<p>
This layer uses Py2PDF for native text extraction and 
PyTesseract for optical character recognition (OCR) if the former 
fails to extract a DOI. The program identifies a DOI 
using a Regex created by CrossRef with a 99% accuracy.
</p>

`Data Verification`
<p>
This layer submits the DOI to CrossRef 
(a database of verified article metadata) 
to fetch the article metadata. If this or any step 
fails the DOI is rejected to maintain the integrity of the
system. 
</p>

`Text Processing`
<p>
This layer formats the fetched metadata according to APA.
It uses NLTK to extract parts of speech, identify nouns 
and apply the APA rules.
</p>

`Zotero Entry`
<p>
This layer receives the formatted data and packages it into
an Zotero article format. It then bundles it with the file 
corresponding PDF file and uploads it to the database.
</p>

### Setup Instructions


### Acknowledgements
* Zotero API
* CrossRef API
* CrossRef DOI Regex
* Google Tesseract
* NLTK