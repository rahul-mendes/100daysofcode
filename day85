from tkinter import *
from PIL import Image, ImageDraw, ImageFont
# to-do 2
# Now we have file path data and text data in GUI, we need to get that here and process it.

def add_watermark():
    image_path = image_input.get()
    watermark = watermark_input.get()

    im = Image.open(image_path)
    width, heigth = im.size

    draw = ImageDraw.Draw(im)
    text = watermark

    font = ImageFont.truetype('arial.ttf, 36')
    textwidht, textheight = draw.textsize(text, font)

    margin = 10
    x = width - textwidht - margin
    y = heigth - textheight - margin

    draw.text((x,y), text, font=font)
    im.show()

    im.save('C:/Users/Omkar/watermark.jpg')

# to-do 1
# Let's design GUI first so that we can have front-end window to dispaly

window = Tk()
window.title("Add a watermark to image")
window.config(padx=20, pady=20)

image_input = Entry(width=70)
image_input.grid(column=1, row=0)

image_label = Label(text="Please provide file path here:")
image_label.grid(column=0, row=0)

watermark_input = Entry(width=70)
watermark_input.grid(column=1, row=1)

watermark_text = Label(text="What text would you like to add as watermark?")
watermark_text.grid(column=0, row=1)

add_watermark_button = Button(text="Add watermark", command=add_watermark)
add_watermark_button.grid(column=1, row=2)

window.mainloop()
