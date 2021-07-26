import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from record import record
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Motion Detector and Video Recorder")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('540x400')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="MOTION DETECTOR")
label_font = font.Font(size=25, weight='bold',family='Century Gothic')
label_title['font'] = label_font
label_title.grid(columnspan=3)


icon = Image.open('icons/spy.png')
icon = icon.resize((100,100), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(columnspan=3)


btn1_image = Image.open('icons/security-camera.png')
btn1_image = btn1_image.resize((30,30), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/recording.png')
btn2_image = btn2_image.resize((30,30), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn3_image = Image.open('icons/exit.png')
btn3_image = btn3_image.resize((30,30), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open('icons/incognito.png')
btn4_image = btn4_image.resize((30,30), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)



# --------------- Button -------------------#


btn_font = font.Font(size=10)
btn3 = tk.Button(frame1, text='Noise', height=40, width=120, fg='green', command=noise, image=btn1_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=3, pady=(20,10), column=0)

btn4 = tk.Button(frame1, text='Record', height=40, width=120, fg='orange', command=record, image=btn2_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=3, pady=(20,10), column=1)


btn6 = tk.Button(frame1, text='In Out', height=40, width=120, fg='green', command=in_out, image=btn4_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=4, pady=(20,10), column=0)

btn5 = tk.Button(frame1, text='Exit', height=40, width=120, fg='red', command=window.quit, image=btn3_image)
btn5['font'] = btn_font
btn5.grid(row=4, pady=(20,10), column=1)

frame1.pack()
window.mainloop()


