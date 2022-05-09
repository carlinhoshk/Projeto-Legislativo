import minecart

pdffile = open('carometro_legislatura56.pdf', 'rb')
doc = minecart.Document(pdffile)

page = doc.get_page(0) # getting a single page

#iterating through all pages
for page in doc.iter_pages():
    im = page.images[0].as_pil()  # requires pillow
    display(im)
