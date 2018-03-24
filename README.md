### Simple Images-to-PDF

A tiny Python program to create a single PDF file from multiple images.

Designed for a computer-illerate user who was losing time while scanning contracts and converted them to PDF.

```
Menu:
1: Create new PDF file
2: Quit

>> 1

Name of new PDF file: test

Path to save location: C:\files\

Path to folder containing images (Ex: "C:/images"): C:\images\

test.pdf created in C:\images\
```

The pages in the PDF output are sorted by the numbers in the image filenames. For example, `"Image01"` comes before `"Image02"`. To be more specific, the filenames are iterated over to see which characters can be converted to integers. These integers are then concatenated and ran through `sort()`.

#### Dependencies:
```
$ pip install Pillow
$ pip install fpdf
```

#### License

MIT.
