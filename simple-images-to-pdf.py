import pathlib
from PIL import Image
from fpdf import FPDF
import re

# check if a full file path is pointed to a image file
def imageCheck(path):
    imageTypes = ['jpg', 'jpeg', 'png', 'gif', 'tiff']
    endOfPath = str(path).split(".")[len(str(path).split(".")) - 1]
    return endOfPath in imageTypes

# collect any numbers from a given string and return them concatinated as an int
def intFromString(string):
    string = str(string)
    final = ''
    for i in string:
        try:
            final += str(int(i))
        except:
            pass
    # if no numbers were found..
    if (final == ''):
        final = '1'
    return int(final) 

# creates a pdf from a list of image file paths
# some source code taken from:
# https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images
def makePdf(pdfFileName, listPages, saveTo, dir = ''):
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]))
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page), 0, 0)

    pdf.output(saveTo + "/" + pdfFileName + ".pdf", "F")

print("Simple Images-to-PDF")
print("- Andrew Healey 2018")
print()

pdfFileName = input("Name of new PDF file: ")
print()
saveLoc = input("Path to save location: ")
print()
folderLoc = input("Path to folder containing images (Ex: \"C:/images\"): ")

listImages = list()
for p in pathlib.Path(folderLoc).iterdir():
    # grab all image files
    if (imageCheck(p)):
        listImages.append(p)

if (len(listImages) == 0):
    raise Exception('No image files found') 

# sort images by any numbers in their filename (concatenated not added)
# if no numbers are found, the page order is random
listImages = sorted(listImages, key=lambda fileName: intFromString(fileName))

makePdf(pdfFileName, listImages, saveLoc)

print()
print(pdfFileName + ".pdf created in in " + saveLoc)
print()
input("Quiting..")
