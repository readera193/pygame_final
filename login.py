from tkinter import Tk, Canvas, YES, BOTH, Frame, Button, Label, Entry, messagebox
from network import Network


class LoginWindow:
    def __init__(self):
        self.win = Tk()
        # reset the window and background color
        self.canvas = Canvas(self.win,
                             width=600, height=500,
                             bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("Digital punch Login")

        self.user_id = ""

    def add_frame(self):
        x, y = 80, 50

        self.frame = Frame(self.win, height=400, width=450)
        self.frame.place(x=x, y=y)

        # now create a login form
        self.label = Label(self.frame, text="Player Login")
        self.label.config(font=("Courier", 40, 'bold'))
        self.label.place(x=x-50, y=y+30)

        self.uidlabel = Label(self.frame, text="User ID:")
        self.uidlabel.config(font=("Courier", 12, 'bold'))
        self.uidlabel.place(x=x-30, y=y+200)

        self.userid = Entry(self.frame, font='Courier 12')
        self.userid.place(x=x+90, y=y+200)

        self.pwdlabel = Label(self.frame, text="Password:")
        self.pwdlabel.config(font=("Courier", 12, 'bold'))
        self.pwdlabel.place(x=x-30, y=y+230)

        self.password = Entry(self.frame, show='*',
                              font='Courier 12')
        self.password.place(x=x+90, y=y+230)

        self.button = Button(self.frame, text="Login",
                             font='Courier 15 bold',
                             command=self.login)
        self.button.place(x=x+90, y=y+260)

        self.win.mainloop()

        return self.user_id

    def login(self):
        # get the data and store it into tuple (data)
        data = (
            self.userid.get(),
            self.password.get()
        )
        # validations
        if self.userid.get() == "":
            messagebox.showinfo("Alert!", "Enter UserID First")
        elif self.password.get() == "":
            messagebox.showinfo("Alert!", "Enter Password First")
        else:
            n = Network()
            res = n.connect({"action": "login", "info": data})
            if res != "None":
                messagebox.showinfo("Message", "Login Successfully")
                self.win.destroy()
                self.user_id = res
            else:
                messagebox.showinfo("Alert!", "Wrong username/password")


def main():
    window = LoginWindow()
    return window.add_frame()
