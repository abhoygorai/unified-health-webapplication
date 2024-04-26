from numpy import *
from keras.models import load_model
from keras.preprocessing import image
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

def wrt(st, fname):
    file = open(fname, "w+")
    file.write(st)
    file.close()

def red(fname):
    file = open(fname, "r")
    f = file.read()
    file.close()
    return f

def open_img():
    try:
        x = openfilename()
        wrt(x, "upload")
        print(x)
        img = Image.open(x)
    except:
        x = 'images/error.png'
        print(x)
        img = Image.open(x)
    img = img.resize((325, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.place(x=455, y=100)

def openfilename():
    filename = filedialog.askopenfilename(title='UPLOAD IMAGE')
    return filename

def callback():
    patient = "\n IMAGE FILE NOT UPLOADED..."
    try:
        model = load_model('models/skin_cancer.h5')
        test_image = image.load_img(red("upload"), target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        result = round(result[0][0])
        patient = "BENIGN" if result == 1 else "MALIGNANT"
        output.set("\n " + patient + " SKIN DETECTED !\n")
        print(patient)
    except Exception as e:
        output.set(patient)
        print("EXCEPTION:", e)

root = Tk()
root.title("SKIN CANCER DETECTOR")
output = StringVar()
root.attributes('-fullscreen', True)

background = PhotoImage(file="images/cover_sc.png")
Label(root, image=background).place(x=0, y=0)

img = Image.open("images/input.png")
img = img.resize((325, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img)
panel.image = img
panel.place(x=455, y=100)

upload = PhotoImage(file=r"images/upload.png")
Button(root, text="upload", bd=0, highlightthickness=0, image=upload,
       command=open_img).place(x=150, y=150)

Label(root, text="\nOUTPUT\n",
      width=25,
      font=("Bauhaus 93", 20)).place(x=432, y=335)
Label(root, text="", textvariable=output,
      font=("Bauhaus 93", 20)).place(x=432, y=335)

detect = PhotoImage(file=r"images/detect.png")
Button(root, text="detect", bd=0, highlightthickness=0, image=detect,
       command=callback).place(x=150, y=340)

close = PhotoImage(file=r"images/home.png")
Button(root, text="close", image=close, highlightthickness=0,
       command=root.destroy).place(x=0, y=0)

root.mainloop()