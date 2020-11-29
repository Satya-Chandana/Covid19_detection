from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image,ImageTk
import numpy as np
from tensorflow.keras.models import load_model
from keras.preprocessing import image


def showimage():
	fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="select a file",filetype=(("jpeg","*.jpeg"),("jpg","*.jpg"),("All files","*.*")))
	img=Image.open(fln)
	img= img.resize((450, 350), Image. ANTIALIAS)
	img=ImageTk.PhotoImage(img)
	lbl.configure(image=img)
	lbl.image=img
	print(fln)


	model_dir = 'model_cnn.h5'
	image_dir = fln #'/content/2.png'

	model_loaded = load_model(model_dir)
	img_width, img_height = 224, 224
	img = image.load_img(image_dir, target_size = (img_width, img_height))
	img = image.img_to_array(img)
	img = np.expand_dims(img, axis = 0)

	result = np.argmax(model_loaded.predict(img), axis=-1)[0]
	
	#self.label.configure(text=self.filename)
	# labelFrame=ttk.LabelFrame(self,text="Select the image file")
	# labelFrame.grid(column=0,row=1,padx=20,pady=20)
	if(result==1):
		#label=tk.LabelFrame(text="COVID19 POSITIVE! TAKE CARE")
		#label.grid(column=300,row=300)
		w = tk.Label(root, text="COVID19 POSITIVE! TAKE CARE")
		w.pack()
		#lab4.config(font=req_font)
		print("COVID19 POSITIVE! TAKE CARE")
	else:
		w = tk.Label(text="COVID19 NEGATIVE! STAY SAFE")
		w.pack()
		#label=tk.LabelFrame(text="COVID19 NEGATIVE! STAY SAFE")
		#label.grid(column=300,row=300)
		print("COVID19 NEGATIVE! STAY SAFE")


root=Tk()
frm=Frame(root)
frm.pack(side=BOTTOM,padx=15,pady=15)

lbl=Label(root)
lbl.pack()

btn=Button(frm,text='browse',command=showimage)
btn.pack(side=tk.LEFT)

btn2=Button(frm,text='exit',command=lambda: exit())
btn2.pack(side=tk.LEFT,padx=10)


root.title("Covid19 detection using customised CNN architecture")
root.geometry("400x500")

root.mainloop()





