import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image

PATH_TO_IMAGE = '/Users/kuba/Pictures/Pictures'
PATH_TO_SAVE = '/Users/kuba/Pictures/Watermark pictures'


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Watermark App")
        self.geometry("200x150")
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)

    @staticmethod
    def work_with_file():
        file = tk.filedialog.askopenfilename(
            initialdir=PATH_TO_IMAGE,
            title='Select a file',
            filetypes=(('PNG', '*.png'), ('JPEG', '*.jpg'))
        )
        if file:
            image = Image.open(file).convert('RGBA')
            watermark = Image.open(f"{PATH_TO_IMAGE}/watermark.jpg").convert("RGBA")

            # Set watermark size
            adjusted_watermark = watermark.resize((round(image.size[0]*.35), round(image.size[1]*.35)))
            watermark_mask = adjusted_watermark.convert('RGBA')

            # Set watermark position
            position = (image.size[0] - adjusted_watermark.size[0], image.size[1] - adjusted_watermark.size[1])

            merge = Image.new('RGBA', image.size)
            merge.paste(image)
            merge.paste(adjusted_watermark, position, mask=watermark_mask)
            # merge.show()

            # # Save photo
            new_photo = merge.convert('RGB')
            # new_photo.save(f"{PATH_TO_SAVE}/image.jpg")

            a = new_photo.filename = asksaveasfilename(
                initialdir=PATH_TO_SAVE,
                title='Save a file',
                filetypes=(('PNG', '*.png'), ('JPEG', '*.jpg')),
            )

            new_photo.save(a)


app = App()
open_button = tk.Button(app, text="Open", command=lambda: App.work_with_file())
quit_button = tk.Button(app, text='Close App', command=lambda: app.destroy())
open_button.pack(padx=20, pady=20)
quit_button.pack(padx=20, pady=30)
app.mainloop()








