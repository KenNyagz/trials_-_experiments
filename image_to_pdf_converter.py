from PIL import Image

# You need a libray called pillow - "pip install Pillow"
image = Image.open('../sample_cv.jpg') # can read jpgs, pngs and other image formats

#Pillow library does not support saving images in the RGBA mode to a PDF. PDF files typically require images in RGB mode.
image = image.convert("RGB") # Convert the image to RGB mode(for those in RGBA), this may not be necessary all the time though

image.save('vwalla.pdf') # save output to file(pdf), with 'pdf' extension
