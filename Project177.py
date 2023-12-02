from tkinter import *

root = Tk()
root.title('Login')
root.geometry('450x450')
root.configure(bg = 'snow')

class Login():
    def __init__(self):
        self.__name = ''
        self.__pasw = ''
        self.__cap = ''
    
    def updateInfo(self):
        self.__name = entName.get()
        self.__pasw = entPasw.get()
        self.__cap = entCap.get()

    def showInfo(self):
        lblInfo['text'] = f'Name: { self.__name }\n\nPassword: { self.__pasw }\n\nCaptcha: { self.__cap }'

login1 = Login()

lblName = Label(root, bg = 'light blue', text = 'Name:')
lblPasw = Label(root, bg = 'light blue', text = 'Password:')
lblCap = Label(root, bg = 'light blue', text = 'Captcha:')
lblInfo = Label(root, bg = 'light blue', text = '')
lblName.place(relx = 0.4, rely = 0.2, anchor = E)
lblPasw.place(relx = 0.4, rely = 0.3, anchor = E)
lblCap.place(relx = 0.4, rely = 0.4, anchor = E)
lblInfo.place(relx = 0.5, rely = 0.6, anchor = N)

entName = Entry(root)
entPasw = Entry(root)
entCap = Entry(root)
entName.place(relx = 0.6, rely = 0.2, anchor = CENTER)
entPasw.place(relx = 0.6, rely = 0.3, anchor = CENTER)
entCap.place(relx = 0.6, rely = 0.4, anchor = CENTER)

btnUpdate = Button(root, text = 'Update Login Info', command = lambda: login1.updateInfo())
btnShow = Button(root, text = 'Show Login Info', command = lambda: login1.showInfo())
btnUpdate.place(relx = 0.35, rely = 0.55, anchor = CENTER)
btnShow.place(relx = 0.65, rely = 0.55, anchor = CENTER)

root.mainloop()