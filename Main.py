from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from PIL import Image
import random

# change the save path according to your OS

savePath = "/Users/bathiyaseneviratne/Desktop/"


def MainMethod():
    try:
        bname = random.randrange(1, 10000)
        gname = random.randrange(1, 10000)
        rname = random.randrange(1, 10000)
        mname = random.randrange(1, 10000)
        doubleblue = random.randrange(1,10000)
        doublegreen = random.randrange(1,10000)
        doublered = random.randrange(1, 10000)

        BluefinalImage = str(bname) + ".jpg"
        GreenfinalImage = str(gname) + ".jpg"
        RedfinalImage = str(rname) + ".jpg"
        MixfinalImage = str(mname) + ".jpg"
        doublebluefinalImage = str(doubleblue) + ".jpg"
        doublegreenfinalImage = str(doublegreen) + ".jpg"
        doubleredfinalImage = str(doublered) + ".jpg"

        path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg'), ("PNG", '.png')])
        img = Image.open(path)
        newImage = img.convert("RGBA")
        r, g, b, a = newImage.split()

        blueimg = Image.merge("RGBA", (b, g, r, a))
        greenimg = Image.merge("RGBA", (g, r, b, a))
        redimg = Image.merge("RGBA", (r, b, g, a))
        miximg = Image.merge("RGBA", (r, b, r, a))
        doubleblueimg = Image.merge("RGBA",(r,b,b,a))
        doublegreenimg = Image.merge("RGBA",(r,g,g,a))
        doubleredimg = Image.merge("RGBA",(r,r,g,a))

        finalBlueImage = blueimg.convert("RGB")
        finalGreenImage = greenimg.convert("RGB")
        finalRedImage = redimg.convert("RGB")
        finalMixImage = miximg.convert("RGB")
        finaldoubleblueImage = doubleblueimg.convert("RGB")
        finaldoublegreenImage = doublegreenimg.convert("RGB")
        finaldoubleredImage = doubleredimg.convert("RGB")

        finalBlueImage.save(savePath + BluefinalImage)
        finalGreenImage.save(savePath + GreenfinalImage)
        finalRedImage.save(savePath + RedfinalImage)
        finalMixImage.save(savePath + MixfinalImage)
        finaldoubleblueImage.save(savePath + doublebluefinalImage)
        finaldoublegreenImage.save(savePath + doublegreenfinalImage)
        finaldoubleredImage.save(savePath + doubleredfinalImage)


        lbl3.config(text="Image status : Generated")


    except:
        tkinter.messagebox.showerror("Error", "No file has been selected")


root = Tk()
root.title("iConverter")
root.resizable(False, False)

window_height = 280
window_width = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

lbl1 = Label(root, text="iConverter")
lbl1.config(font=("Helvetica bold", 20))
lbl1.pack(pady=10)

lbl3 = Label(root, text="Image status : Pending")
lbl3.config(font=("Arial", 15))
lbl3.pack(pady=10)

lbl2 = Label(root, text="Developed by Bathiya Seneviratne", fg="red", font=("Arial", 12), bg="#f1f1f1")
lbl2.pack(side=BOTTOM, fill=X)

but = Button(root, text="Select & Save", width=20, height=2, command=MainMethod)
but.pack(side=BOTTOM, pady=10)

root.mainloop()
