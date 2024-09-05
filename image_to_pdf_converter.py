from PIL import Image

# You need a libray called pillow - "pip install Pillow"
image = Image.open('../sample_cv.jpg') # can read jpgs, pngs and other image formats

image.save('vwalla.pdf') # save output to file(pdf), with 'pdf' extension
