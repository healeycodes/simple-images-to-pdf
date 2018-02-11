## simple-images-to-pdf


### Requires Python 3.4+
### Works with PyInstaller

Dependencies:

`$ pip install Pillow`

`$ pip install fpdf`

## Features

Creates a single PDF file from multiple images. I wrote this to aid people who need to create PDFs from scanned-in files.

A typical run looks like this:

```
Simple Images-to-PDF
- Andrew Healey 2018

Name of PDF file (without file extension): test

Path to folder containing .jpg images (Ex: "C:\images"): C:\test-images

test.pdf is located in C:\test-images

Quiting..
```

The pages in the PDF output are sorted by the numbers in the source images' filenames.

`listImages = sorted(listImages, key=lambda fileName: intFromString(fileName))`

`intFromString()` reduces filename strings down to just integers, e.g., `"image of boat 12"` becomes `12`

If there are no integers in the filenames, the page order is random.
