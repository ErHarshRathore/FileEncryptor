from tkinter import Tk,Frame,PhotoImage
from appPages import init,title_bar,startPage

app = Tk()
init(app)
app.overrideredirect(1)
app.attributes('-topmost',1)
app.grid_propagate(False)
app.title('File Encryptor')

halfx = str(app.winfo_screenwidth() //2 - 400)
halfy = str(app.winfo_screenheight()//2 - 240)
app.geometry('800x480+' + halfx + '+' +halfy)
del halfx,halfy

app.iconbitmap('logo.ico')
app.bind('<Map>',lambda e:app.overrideredirect(1))

titleFrm = Frame(app,width=800,height=30,bg='#666')
icon = PhotoImage(file=r'CryptoIcon.png')
title_bar(titleFrm,'File Encryptor',icon)

bodyFrm = Frame(app,width=800,height=450,bg='#efefef')
bg1 = PhotoImage(file=r'logo.png',width=860,height=450)
bg2 = PhotoImage(file=r'bg1.png' ,width=300,height=300)
startPage(bodyFrm,bg1,bg2)

titleFrm.grid(row=0,column=0)
bodyFrm .grid(row=1,column=0)

app.mainloop()
