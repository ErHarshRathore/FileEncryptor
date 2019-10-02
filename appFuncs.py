help_flag = False

def init(app):
      global _app
      _app = app

def close_window():
      global _app,help_window
      _app.destroy()
      try:
            help_window.destroy()
      except:
            pass

def minmz_window():
      global _app
      _app.withdraw()
      _app.overrideredirect(0)
      _app.iconify()

def helpp_window():
      global help_flag,_app,help_window
      
      if help_flag : return
      def set_flag(boolean):
            global help_flag
            help_flag = boolean
            
      help_flag = True
      from tkinter import Tk,Text,Label,mainloop
      help_window = Tk();pos = _app.geometry().split('+')[1:]
      help_window . geometry('800x450+' + pos[0] + '+' + str(int(pos[1])+30))
      help_window . overrideredirect(1);help_window . attributes('-topmost',1)
      help_window . bind('<Destroy>',lambda e:set_flag(False))

      document = Text(help_window,font='"times" 16 italic bold',border=0)
      document . insert('1.0',open('documentation.txt','r').read())
      document . config(bg='#eee',width=73,height=19,state='disable',selectbackground='#f90')#73x19@16
      document . place(x=0,y=0)
      
      close_btn = Label(help_window,text='x',bg='#f00',fg='#eee',font='"" 15 bold',width=2)
      close_btn . bind('<ButtonRelease-1>',lambda e: help_window.destroy())
      close_btn . place(x=770,y=422)

      cpyright = 'copyright© Er. Harsh Rathore'
      cpyright = Label(help_window,text=cpyright,fg='#f00')
      cpyright . place(x=0,y=430)

      help_window . mainloop()

def drag(event):
      global _app
      t = _app.geometry().split('+')[1:]
      xval = int(t[0])
      yval = int(t[1])
      del t
      _app.geometry('+'+
                  str(xval+ event.x -400)+
                  '+'+str(yval + event.y -20))

def get_key(str_key):   #will return a int with raspective key
      key=''
      for ch in str_key:
            ch = bin(ord(ch))[2:]
            ch = '0'*(7-len(ch))+ch
            key += ch
      return int(key,2)

def ran_key(length):    #will return a inputable and readable random key
	from random import choice,randint
	key=''
	for i in range(length):
		key+=chr(choice((randint(32,126),randint(65,90),randint(97,122))))
	return key
