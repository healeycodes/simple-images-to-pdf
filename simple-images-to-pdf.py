import pathlib
from PIL import Image
from fpdf import FPDF
import re

# check if a full file path is pointed to a image file
def image_check(path):
    image_types = ['jpg', 'jpeg', 'png', 'gif', 'tiff']
    end_of_path = str(path).split(".")[len(str(path).split(".")) - 1]
    return end_of_path in image_types

# collect any numbers from a given string and return them concatinated as an int
def int_from_string(string):
    string = str(string)
    final = ''
    for i in string:
        try:
            final += str(int(i))
        except:
            pass
    # if no numbers could be found, just return '1'
    if (final == ''):
        final = '1'
    return int(final) 

# creates a pdf from a list of image file paths
def make_pdf(pdf_filename, listPages, saveTo, dir = ''):
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]))
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page), 0, 0)

    pdf.output(saveTo + "/" + pdf_filename + ".pdf", "F")

def create_new_pdf():
    print()
    pdf_filename = input("Name of new PDF file: ")
    print()
    save_location = input("Path to save location: ")
    print()
    folder_location = input("Path to folder containing images (Ex: \"C:/images\"): ")

    list_images = list()
    for p in pathlib.Path(folder_location).iterdir():
        # grab all image files
        if (image_check(p)):
            list_images.append(p)

    if (len(list_images) == 0):
        raise Exception('No image files found') 

    # sort images by any numbers in their filename (concatenated not added)
    # if no numbers are found, the page order is random
    list_images = sorted(list_images, key=lambda fileName: int_from_string(fileName))

    make_pdf(pdf_filename, list_images, save_location)

    print()
    print(pdf_filename + ".pdf created in " + save_location)
    program_loop()

def program_loop():

    while True:
        print('\nMenu:')
        print('1: Create new PDF file')
        print('2: Quit\n')
        user_input = input('>> ')

        if(user_input == '1'):
            create_new_pdf()
        if(user_input == '2'):
            break
        else:
            break

# start program
print('Simple Images-to-PDF\n')
program_loop()