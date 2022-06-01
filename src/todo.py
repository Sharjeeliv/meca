# This problem will have 3 key components: Extraction, Verification, Entry
# TODO : 1. Extract metadata from pdf documents ~2400
# A. Determine method for OCR extraction (OpenCV & PyTesseract)
# B. Method for text extraction (Py2PDF)
# C. Locate the information from within the file
# D. For efficiency consider only searching the first page, determine priority of metadata (only need 1 to search)
# E. Flagging for any file that can not be read and/or move that file to a folder with path info

# TODO : 2. Verify the validity of the metadata using either the extracted DOI or Title
# A. Determine method on verification for different input data
# B. Priority List of data is: i. DOI, ii. Author and Title
# Separate flagging for handling unverifiable data and sort it out.

# TODO : 3. Format data for entry to Zotero database
# A. Title (lower case except for first word and nouns)
# B. Author (last name + first name (full or initial) + any other initial if applicable)
# C. Publication (name of the journal outlet)
# D. Volume (almost always exists)
# E. Issue No (sometimes does not exist - almost always appears right after the volume): i. Handling for data not found
# F. Pages
# G. DOI ** This is a very

# TODO: 4. Automate data entry to Zotero
# A. Verification and connection with Zotero API
# B. Control input flow (do not want to get blocked for excessive strain)
# C. Input verified information ~ Attached the original file (heavy i/o load)
# D. Determine the organization... Possibly do one folder at a time

# TODO: 5. Into Production
# A. With all testing and development complete cautiously port all
# Actual files from local device to Zotero
