import tkinter as tkk
from appFuncs import *

selectedMenu = 0

def init(root):
      global base
      import appFuncs as af
      af.init(root)
      base = root

def title_bar(titleFrm,title='',icon=None):
      titleFrm . pack_propagate(False)
      titleFrm.bind('<B1-Motion>',drag)
      appFont = 'ROD 18 bold'
      
      global base
      
      appIcon = tkk.Label(titleFrm,image=icon,width=30,height=22)
      appIcon . place(x=6,y=3)

      appTitle = tkk.Label(titleFrm,text=title,fg='#f90') #ff7060 for original
      appTitle . config(font=appFont,bg='#666')
      appTitle . place(x=44,y=0)
      appTitle . bind('<B1-Motion>',drag)

      closeBtn = tkk.Label(titleFrm,text='x',fg='#eee')
      closeBtn . config(font=appFont,bg='#666',width=2)
      closeBtn . place(x=764,y=0)
      closeBtn . bind('<ButtonRelease-1>',lambda e:close_window())
      closeBtn . bind('<Enter>',lambda e: closeBtn.config(bg='#f00'))
      closeBtn . bind('<Leave>',lambda e: closeBtn.config(bg='#666'))

      minmzBtn = tkk.Label(titleFrm,text='-',fg='#eee')
      minmzBtn . config(font=appFont,bg='#666',width=2)
      minmzBtn . place(x=731,y=0)
      minmzBtn . bind('<ButtonRelease-1>',lambda e:minmz_window())
      minmzBtn . bind('<Enter>',lambda e: minmzBtn.config(bg='#0cf'))
      minmzBtn . bind('<Leave>',lambda e: minmzBtn.config(bg='#666'))

      helpBtn = tkk.Label(titleFrm,text='?',fg='#eee')
      helpBtn . config(font=appFont,bg='#666',width=2)
      helpBtn . place(x=697,y=0)
      helpBtn . bind('<ButtonRelease-1>',lambda e:helpp_window())
      helpBtn . bind('<Enter>',lambda e: helpBtn.config(bg='#999'))
      helpBtn . bind('<Leave>',lambda e: helpBtn.config(bg='#666'))


def startPage(bodyFrm,bg1,bg2):
      bodyFrm . pack_propagate(False)
      
      backgrnd1 = tkk.Label(bodyFrm,image=bg1,width=800,height=450)
      backgrnd1 . place(x=26,y=0)

      backgrnd2 = tkk.Label(bodyFrm,image=bg2,width=300,height=300)
      backgrnd2 . place(x=455,y=50)

      msgPage1 = "Keep your data Hidden\nand Secure with Us"
      msgPage1 = tkk.Label(bodyFrm,text=msgPage1,bg='#efefef',fg='#666',width=22,font='ARIAL 17')
      msgPage1 . place(x=456,y=260)

      startApp = tkk.Label(bodyFrm,text='Get Start',width=14,bg='#666',fg='#eee',font='CONSOL 24 bold')
      startApp . place(x=468,y=350)
      startApp . bind('<Enter>',lambda e:startApp.config(bg='#f90'))
      startApp . bind('<Leave>',lambda e:startApp.config(bg='#666'))
      startApp . bind('<ButtonRelease-1>',lambda e:onClickStartApp())

      cpyright = 'copyright© Er. Harsh Rathore'
      cpyright = tkk.Label(bodyFrm,text=cpyright,fg='#f00')
      cpyright . place(x=634,y=430)

      def cleaner():
            cpyright .destroy()
            backgrnd1.destroy()
            backgrnd2.destroy() 
            msgPage1 .destroy()
            startApp .destroy()

      def onClickStartApp():
            cleaner()
            homePage(bodyFrm)
      
def homePage(bodyFrm):

      sideFrm = tkk.Frame(bodyFrm,bg='#666',width=140,height=450)
      sideFrm . place(x=0,y=0)

      global mainFrm
      mainFrm = tkk.Frame(bodyFrm,bg='#444',width=660,height=450)
      mainFrm . place(x=140,y=0)

      cpyright = 'copyright©Er.Harsh Rathore'
      cpyright = tkk.Label(sideFrm,text=cpyright,bg='#666',fg='#777',font='"" 8')
      cpyright . place(x=0,y=432)

      sideMenu(sideFrm)
      
def sideMenu(sideFrm):  #Side Menu Frame for option menues
      lstBox = tkk.Listbox(sideFrm,width=11,height=10,borderwidth=0,bg='#666')
      lstBox . config(highlightthickness=0,font='"" 18 bold',justify='center')
      lstBox . config(fg='#f90',selectbackground='#444',selectforeground='#0cf')
      lstBox . place(x=0,y=-5)      
      lstBox . insert(0,'')
      lstBox . insert(1,'Encryption')
      lstBox . insert(2,'')
      lstBox . insert(3,'Decryption')
      lstBox . insert(4,'')
      lstBox . insert(5,'New Key')
      lstBox . insert(6,'')
      lstBox . insert(7,'About Us')
      lstBox . selection_set(1)

      initGUI()
      updateMainBody(1)

      def clearselect(event):
            try:
                  var=lstBox.curselection()[0]
                  if var%2 == 0: 
                        event.widget.select_clear(var)
                        var += 1
                  updateMainBody(var)
            except:
                  global selectedMenu
                  var = selectedMenu
            event.widget.select_set(var)
      lstBox.bind('<<ListboxSelect>>',clearselect)

def updateMainBody(mainPage):
      global selectedMenu
      if selectedMenu == mainPage:  return

      global curMainFrm,encBFrm
      selectedMenu = mainPage
      curMainFrm . place_forget()
      if   mainPage==1: curMainFrm = encBFrm
      elif mainPage==3: curMainFrm = decBFrm
      elif mainPage==5: curMainFrm = keyBFrm
      elif mainPage==7: curMainFrm = abtBFrm
      curMainFrm . place(x=0,y=0)

def proceedEvent():
      global curMainFrm,encBFrm,decBFrm
      from tkinter import messagebox

      try:
            techDic = {' 32 bits':(5,4),' 64 bits':(6,9),'128 bits':(7,18),'256 bits':(8,36)}
            dicFrm = curMainFrm.children
            filename = dicFrm['!frame'].children['!entry'].get()
            file = open(filename,'r',encoding='utf-8')
            file . seek(0)
            method=dicFrm['!frame2'].children['!optionmenu']
            key  = dicFrm['!frame3'].children['!entry'].get()
            data = file.read()
            if curMainFrm == encBFrm :
                  from Crypt import Encryption
                  tech = techDic[method.getvar('PY_VAR0')][0]
                  print('length of key =',len(key))
                  if len(key) <= techDic[method.getvar('PY_VAR0')][1]:
                        key = get_key(key)
                  else:
                        raise Exception('keyError : Invalid Key')
                  e = Encryption(tech,data,key)
                  cipher = e.Encrypt()
                  newf = open(filename+'.enc','w',encoding='utf-8')
                  newf . write(cipher)
      
            elif curMainFrm == decBFrm:
                  from Crypt import Decryption
                  tech = techDic[method.getvar('PY_VAR1')][0]
                  if len(key) <= techDic[method.getvar('PY_VAR1')][1]:
                        key = get_key(key)
                  else:
                        raise Exception('keyError : Invalid Key')
                  d = Decryption(tech,data,key)
                  message = d.Decrypt()
                  newf = open(filename+'.txt','w',encoding='utf-8')
                  newf . write(message)
            newf . flush()
            newf . close()
            messagebox.showinfo ('Succeed','You have a new file Now')
      except:
            messagebox.showerror('Failed','An Error Occurred,\ncheck the Key or File type')

def cancelEvent():
      global curMainFrm,encBFrm

      dicFrm = curMainFrm.children
      dicFrm['!frame'].children['!entry'].delete(0,500)
      if curMainFrm == encBFrm:
            curMainFrm.setvar('PY_VAR0',' 32 bits')
      else:
            curMainFrm.setvar('PY_VAR1',' 32 bits')
      dicFrm['!frame3'].children['!entry'].delete(0,500)

def generateKeyEvent():
      global curMainFrm

      dicFrm = curMainFrm.children
      techDic = {' 32 bits':4,' 64 bits':9,'128 bits':18,'256 bits':36}
      tech = techDic[dicFrm['!frame'].children['!optionmenu'].getvar('PY_VAR2')]

      entry = dicFrm['!frame2'].children['!entry']
      entry . delete(0,len(entry.get()))
      entry . insert(0,ran_key(tech))

def initGUI():
      global encBFrm,decBFrm,keyBFrm,abtBFrm
      global curMainFrm,mainFrm

      encBFrm = tkk.Frame(mainFrm,bg='#444',width=660,height=450)
      decBFrm = tkk.Frame(mainFrm,bg='#444',width=660,height=450)
      keyBFrm = tkk.Frame(mainFrm,bg='#444',width=660,height=450)
      abtBFrm = tkk.Frame(mainFrm,bg='#444',width=660,height=450)

      initEnc(encBFrm)  #initialize Encryption Frame
      initDec(decBFrm)  #initialize Decryption Frame
      initKey(keyBFrm)  #initialize Random Key Frame
      initAbt(abtBFrm)  #initialize About Us   Frame

      curMainFrm = encBFrm    #set Encryption Frame as Home page

def fileFrm(frame):     #Components for input file frame
      ft,bg,fg="'' 14 bold",'#444','#aaa'

      tkk.Label(frame,text='Select a File :',font=ft,bg=bg,fg=fg).place(x=10)
      
      entredFile = tkk.Entry(frame,width=30,font=ft)
      entredFile . place(x=150)
      entredFile . unbind_all(('<VirtualEvent>','<Double-1>'))

      opener = tkk.Label(frame,text='Open',width=5,font=ft,fg='#fff',bg='#f90')
      opener . place(x=520)
      opener.bind('<Enter>',lambda e:opener.config(bg='#0cf'))
      opener.bind('<Leave>',lambda e:opener.config(bg='#f90'))
      
      from tkinter.filedialog import askopenfile as aof
      def fileOpener(event):
            entredFile.delete(0,len(entredFile.get()))
            entredFile.insert(0,aof().name)
      opener.bind('<ButtonRelease-1>',fileOpener)
      return frame

def techFrm(frame):     #Components for get Method frame
      ft,bg,fg="'' 14 bold",'#444','#aaa'

      tkk.Label(frame,text="Technique :",font=ft,bg=bg,fg=fg).place(x=10)

      val = tkk.StringVar(frame,' 32 bits')
      optnM=tkk.OptionMenu(frame,val,' 32 bits',' 64 bits','128 bits','256 bits')
      optnM.config(width=26,border=0,bg=bg,fg=fg,font=ft)
      optnM.place(x=150)

      global mainTech
      mainTech = val
      return frame

def keyFrm(frame):      #Components for get Key frame
      ft,bg,fg="'' 14 bold",'#444','#aaa'

      tkk.Label(frame,text="Key :",font=ft,bg=bg,fg=fg).place(x=10)

      entredKey=tkk.Entry(frame,width=30,font=ft)
      entredKey.place(x=150)
      entredKey.unbind_all(('<VirtualEvent>','<Double-1>'))

      return frame

def btnFrmCP(frame):    #Components for Cancel and Proceed frame
      ft,bg="'' 14 bold",'#0cf'

      cancelBTN = tkk.Label(frame,text='Cancel',width=13,font=ft,fg='#fff',bg='#f00')
      cancelBTN.place(x=150)
      cancelBTN.bind('<Button-1>',lambda e:cancelEvent())
      cancelBTN.bind('<Enter>',lambda e:cancelBTN.config(bg=bg))
      cancelBTN.bind('<Leave>',lambda e:cancelBTN.config(bg='#f00'))

      proceedBTN = tkk.Label(frame,text='Proceed',width=13,font=ft,fg='#fff',bg='#0c0')
      proceedBTN.place(x=320)
      proceedBTN.bind('<Button-1>',lambda e:proceedEvent())
      proceedBTN.bind('<Enter>',lambda e:proceedBTN.config(bg=bg))
      proceedBTN.bind('<Leave>',lambda e:proceedBTN.config(bg='#0c0'))

      return frame

def btnFrmGK(frame):    #Component for Generate key Frame
      ft,bg="'' 14 bold",'#0cf'

      proceedBTN = tkk.Label(frame,text='Generate New Key',width=28,fg='#eee',font=ft,bg='#0c0')
      proceedBTN.place(x=146)
      proceedBTN.bind('<Button-1>',lambda e:generateKeyEvent())
      proceedBTN.bind('<Enter>',lambda e:proceedBTN.config(bg=bg))
      proceedBTN.bind('<Leave>',lambda e:proceedBTN.config(bg='#0c0'))

      return frame

def initEnc(frame):     #Add Elements in Encryption frame
      filef = fileFrm(tkk.Frame(frame,bg='#444',width=660,height=45))
      filef.place(x=0,y=50)

      techf = techFrm(tkk.Frame(frame,bg='#444',width=660,height=45))
      techf.place(x=0,y=150)

      keyf  = keyFrm(tkk.Frame(frame,bg='#444',width=660,height=45))
      keyf.place(x=0,y=250)

      btnf = btnFrmCP(tkk.Frame(frame,bg='#444',width=660,height=45))
      btnf.place(x=0,y=350)

def initDec(frame):     #Add Elements in Decryption frame
      filef = fileFrm(tkk.Frame(frame,bg='#444',width=660,height=45))
      filef.place(x=0,y=50)

      techf = techFrm(tkk.Frame(frame,bg='#444',width=660,height=45))
      techf.place(x=0,y=150)

      keyf  = keyFrm(tkk.Frame(frame,bg='#444',width=660,height=45))
      keyf.place(x=0,y=250)

      btnf = btnFrmCP(tkk.Frame(frame,bg='#444',width=660,height=45))
      btnf.place(x=0,y=350)

def initKey(frame):     #Add Elements in Random Key frame
      techf = techFrm(tkk.Frame(frame,bg='#444',width=660,height=45))
      techf.place(x=0,y=100)

      keyf  = keyFrm(tkk.Frame(frame,bg='#444',width=660,height=45))
      keyf.place(x=0,y=225)

      btnf = btnFrmGK(tkk.Frame(frame,bg='#444',width=660,height=45))
      btnf.place(x=0,y=350)

def initAbt(frame):     #Add Elements in About Us frame
      text = tkk.Text(frame,font='times 14 italic bold',selectbackground='red')
      text . config(width=64,height=19,border=0)
      text . insert('1.0',open('about.txt','r').read())
      text . config(bg='#444',fg='#f90',state='disable')
      text . place(x=10,y=6)

      def openLink(link):
            from os import popen
            popen('start /max '+link)
            minmz_window()

      mysite= tkk.Label(frame,text='Er.Harsh Rathore',font='times 12 italic',fg='#eee',bg='#444')
      mysite. place(x=10,y=425)
      mysite. bind('<Enter>',lambda e:mysite.config(fg='#0cf'))
      mysite. bind('<Leave>',lambda e:mysite.config(fg='#eee'))
      mysite. bind('<Button-1>',lambda e:openLink('http://erharshrathore.000webhostapp.com'))

      sof = tkk.Label(frame,text='StackOverflow',font='times 12 italic',fg='#eee',bg='#444')
      sof . place(x=180,y=425)
      sof . bind('<Enter>',lambda e:sof.config(fg='#0cf'))
      sof . bind('<Leave>',lambda e:sof.config(fg='#eee'))
      sof . bind('<Button-1>',lambda e:openLink('https://stackoverflow.com/users/10180730/er-harsh-rathore'))

      insta = tkk.Label(frame,text='Instagram',font='times 12 italic',fg='#eee',bg='#444')
      insta . place(x=334,y=425)
      insta . bind('<Enter>',lambda e:insta.config(fg='#0cf'))
      insta . bind('<Leave>',lambda e:insta.config(fg='#eee'))
      insta . bind('<Button-1>',lambda e:openLink('https://instagram.com/er.harsh_rathore'))

      whats = tkk.Label(frame,text='WhatsApp',font='times 12 italic',fg='#eee',bg='#444')
      whats . place(x=466,y=425)
      whats . bind('<Enter>',lambda e:whats.config(fg='#0cf'))
      whats . bind('<Leave>',lambda e:whats.config(fg='#eee'))
      whats . bind('<Button-1>',lambda e:openLink('https://api.whatsapp.com/send?phone=917879121927'))

      tweet = tkk.Label(frame,text='Twitter',font='times 12 italic',fg='#eee',bg='#444')
      tweet . place(x=590,y=425)
      tweet . bind('<Enter>',lambda e:tweet.config(fg='#0cf'))
      tweet . bind('<Leave>',lambda e:tweet.config(fg='#eee'))
      tweet . bind('<Button-1>',lambda e:openLink('https://twitter.com/ErHarshRathore'))
