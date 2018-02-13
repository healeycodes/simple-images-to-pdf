## Simple Images-to-PDF


### Requires Python
#### Works with PyInstaller

Dependencies:

`$ pip install Pillow`

`$ pip install fpdf`

## Features

Creates a single PDF file from multiple images.

The initial use case was for a computer illerate user who was scanning contracts.

Currently searches for JPG files only but the script is well commented and highly extensible.

A typical run looks like this:

```
Simple Images-to-PDF
- Andrew Healey 2018

Name of new PDF file: test

Path to save location: C:/test-images

Path to folder containing images (Ex: \"C:/images/"): C:/test-images

test.pdf created in C:/test-images

Quiting..
```

The pages in the PDF output are sorted by the numbers in the source images' filenames, e.g., Image01 then Image02

`intFromString()` reduces filename strings down to just integers, e.g., `"image of boat 12"` becomes `12`

If there aren't any numbers in the filenames, the page order is random.
