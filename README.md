## Simple Images-to-PDF


### Requires Python
#### Works with PyInstaller

Dependencies:

`$ pip install Pillow`

`$ pip install fpdf`

## Features

Creates a single PDF file from multiple images.

The initial use case was for a computer illerate user who was scanning contracts.

A typical run looks like this:

```
Name of new PDF file: test

Path to save location: C:/test-images

Path to folder containing images (Ex: "C:/images"): C:/test-images

test.pdf created in C:/test-images

Quiting..
```

The pages in the PDF output are sorted by the numbers in the image filenames. For example, `"Image01"` comes before `"Image02"`. To be more specific, the filenames are iterated over to see which characters can be converted to integers. These integers are then concatenated and ran through `sort()`.
