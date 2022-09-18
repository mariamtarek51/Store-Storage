import verify as v
import items as it
import pandas as pd
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
from PIL import Image
import storeStorage as st
from tkinter import filedialog, messagebox
from tkinter.simpledialog import askinteger
import tkinter as tk
from tkinter import messagebox

# In[2]:
""" 
Function:store storage Gui 
user can sign in or sign up and set values for items 
version :v3
Date:16/9/2022 
authors:mariam



"""
def set_helper(obj1,element,frame):
    """
    get the new value from the user

    :param obj1: object which has list of items
    :param element: the name of element i want change its value
    :param frame: frame name in which element created
    :return:none
    """

    prompt = askinteger("Integer", "Enter your new value")
    print(prompt)
    if(prompt):
        obj1.set_(element, str(prompt))
        print(obj1.getlist())
        frame["text"] = element + "\n" + str(prompt)




def listwindow(data,obj1):
    """
    represent list of items user has
    :param data: dic of items
    :param obj1: object which has list of items 
    :return: none
    """""
    print("im in list window")
    print(data);
    signIn.destroy()

    list_window=tk.Tk()
    list_window.title("list window")
    center_screen(list_window)
    items_no=len(data.keys())
    print("items no",items_no)

    # Constructing the first frame, frame1
    frame1 = tk.LabelFrame(list_window, text=str(list((data.keys()))[0])+"\n"+str(list((data.values()))[0]), bg="#d4dceb",
                        fg="black",font=('calibre', 15, 'bold') ,padx=76, pady=30)

    # Displaying the frame1 in row 0 and column 0
    frame1.grid(row=0, column=0)

    # Constructing the button b1 in frame1
    b1 = tk.Button(frame1, text="set",font=('calibre', 15, 'bold'),command=lambda :set_helper(obj1,list((data.keys()))[0],frame1))

    # Displaying the button b1
    b1.pack()

    # Constructing the second frame, frame2
    frame2 = tk.LabelFrame(list_window, text=str(list((data.keys()))[1])+"\n"+str(list((data.values()))[1]),fg="white" ,bg="#283d9d",font=('calibre', 15, 'bold'), padx=76, pady=30)

    # Displaying the frame2 in row 0 and column 1
    frame2.grid(row=0, column=2)

    # Constructing the button in frame2
    b2 = tk.Button(frame2, text="set",font=('calibre', 15, 'bold'),command=lambda :set_helper(obj1,list((data.keys()))[1],frame2))

    # Displaying the button b2
    b2.pack()
    frame3 = tk.LabelFrame(list_window, text=str(list((data.keys()))[2])+"\n"+str(list((data.values()))[2]), bg="#d4dceb",font=('calibre', 15, 'bold'), padx=76, pady=30)

    # Displaying the frame2 in row 0 and column 1
    frame3.grid(row=0, column=4)

    # Constructing the button in frame2
    b3 = tk.Button(frame3, text="set",font=('calibre', 15, 'bold'),command=lambda :set_helper(obj1,list((data.keys()))[2],frame3))

    # Displaying the button b2
    b3.pack()
    frame4 = tk.LabelFrame(list_window, text=str(list((data.keys()))[3])+"\n"+str(list((data.values()))[3]), bg="#283d9d",
                           fg="white",font=('calibre', 15, 'bold'), padx=76, pady=30)

    # Displaying the frame1 in row 0 and column 0
    frame4.grid(row=1, column=0)

    # Constructing the button b1 in frame1
    b4 = tk.Button(frame4, text="Set",font=('calibre', 15, 'bold'),command=lambda :set_helper(obj1,list((data.keys()))[3],frame4))

    # Displaying the button b1
    b4.pack()

    # Constructing the second frame, frame2
    frame5 = tk.LabelFrame(list_window, text=str(list((data.keys()))[4])+"\n"+str(list((data.values()))[4]), bg="#d4dceb",font=('calibre', 15, 'bold'), padx=76, pady=30)

    # Displaying the frame2 in row 0 and column 1
    frame5.grid(row=1, column=2)

    # Constructing the button in frame2
    b5 = tk.Button(frame5, text="set",font=('calibre', 15, 'bold'),command=lambda :set_helper(obj1,list((data.keys()))[4],frame5))

    # Displaying the button b2
    b5.pack()
    frame6 = tk.LabelFrame(list_window, text=str(list((data.keys()))[5])+"\n"+str(list((data.values()))[5]), bg="#283d9d",fg="white" ,font=('calibre', 15, 'bold'), padx=76, pady=30)

    # Displaying the frame2 in row 0 and column 1
    frame6.grid(row=1, column=4)


    # Constructing the button in frame2
    b6 = tk.Button(frame6, text="set",font=('calibre', 15, 'bold'),command=lambda :set_helper(obj1,list((data.keys()))[5],frame6))

    # Displaying the button b2
    b6.pack()




def start():
    """
    when a user clicks sign in,this function deals with warning messages and check email

    :return:
    """



    global counter

    print("im in start finally ")
    print(type(email_var))


    print("email var is",email_var.get())
    print("passw_var is",passw_var.get())
   # email_var.trace("w", lambda *args:pg.typewrite(email_var.get(), interval=0.2))

    #print(str(email_var.get()))
    if v.valid_email(str(email_var.get())):


        found, line, line_index = v.check_email(str(email_var.get()), "t.txt")
        print(line)
        print(line_index)

        if found:
            print("found is ",found)
            pass_f = line.strip('\n').split(' ')[1]
            print("savedpass : ",pass_f)
            print("entered_pass",passw_var.get())

            if(counter!=0):
                entered_pass=str(passw_var.get())
                if (v.verify_password(str(pass_f),entered_pass)==False):
                    print("counter in false ",counter)
                    passw_var.set("")
                    messagebox.showwarning("incorrect Password", "your Password is incorrect")




                    counter=counter-1

                else:
                    #email &passw is valid
                    storelist,obj1=st.show_list(line_index, "data.csv")
                    listwindow(storelist,obj1)
                    counter=0;
            else:
                print("counter in else",counter)
                signIn.destroy()

        else:
            print("your email is not found")
            email_var.set("")
            passw_var.set("")
            messagebox.showinfo("not found", "your email is not found")

    else :
        print("invalid username ")
        email_var.set("")
        passw_var.set("")
        messagebox.showinfo("invalid", "invalid username,should end with @qz.com")


def center_screen(window):
    """ gets the coordinates of the center of the screen
    :param window: which window i wanna center

     """
    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # Coordinates of the upper left corner of the window to make the window appear in the center
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
def signinwindow():
    """
    display sign in window
    :return:
    """
    #global email_var
   # global passw_var
    global signIn
    global passw_entry
    signIn = tk.Tk()

    #wel_label = tk.Label(root, text='Welcome to our store ', font=('calibre', 15, 'bold'))
    #wel_label.place(relx=0.5, rely=0.1, anchor="center")

    root.destroy()
    createvar(signIn)
    signIn.title("sign in ")
    center_screen(signIn)

    sign_label = tk.Label(signIn, text='sign in ', font=('calibre', 15, 'bold'))
    sign_label.place(relx=0.5, rely=0.2, anchor="center")

    name_label = tk.Label(signIn, text='Username', font=('calibre', 10, 'bold'))
    name_label.place(relx=0.3, rely=0.3, anchor="center")

    name_entry = tk.Entry(signIn,textvariable=email_var, font=('calibre', 10, 'normal'))
    name_entry.place(relx=0.5, rely=0.3, anchor="center")




    passw_label = tk.Label(signIn, text='Password', font=('calibre', 10, 'bold'))
    passw_label.place(relx=0.3, rely=0.4, anchor="center")

    passw_entry = tk.Entry(signIn,textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
    passw_entry.place(relx=0.5, rely=0.4, anchor="center")


    sub_btn = tk.Button(signIn, text='Sign in',command =lambda :start())
    sub_btn.place(relx=0.5, rely=0.5, anchor="center")
    signIn.mainloop()
def createvar(window):
    """
    create string var for a window
    :param window: tk window
    :return:
    """
    global email_var
    global passw_var
    email_var = tk.StringVar(window, "")
    passw_var = tk.StringVar(window, "")
def signup_helper():
    """
    check if email is valid
    :return:
    """
    print("in sign up helper")
    print("email is ",str(email_var.get()))
    if(v.valid_email(str(email_var.get()))):
        v.sign_up(str(email_var.get()), passw_var.get(), "t.txt", "data.csv")
        signup.destroy()
    else:
        print("invalid username ")
        email_var.set("")
        passw_var.set("")
        messagebox.showinfo("invalid", "invalid username,should end with @qz.com")



def signupwindow():
    """
    display sign up window
    :return: none
    """

    global signup
    global passw_entry
    signup = tk.Tk()


    root.destroy()
    createvar(signup)
    signup.title("sign up ")
    center_screen(signup)

    sigu_label = tk.Label(signup, text='Sign Up ', font=('calibre', 15, 'bold'))
    sigu_label.place(relx=0.5, rely=0.2, anchor="center")

    name_label = tk.Label(signup, text='Username', font=('calibre', 10, 'bold'))
    name_label.place(relx=0.3, rely=0.3, anchor="center")

    name_entry = tk.Entry(signup,textvariable=email_var, font=('calibre', 10, 'normal'))
    name_entry.place(relx=0.5, rely=0.3, anchor="center")




    passw_label = tk.Label(signup, text='Password', font=('calibre', 10, 'bold'))
    passw_label.place(relx=0.3, rely=0.4, anchor="center")

    passw_entry = tk.Entry(signup,textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
    passw_entry.place(relx=0.5, rely=0.4, anchor="center")


    sub_btn = tk.Button(signup, text='OK',command =lambda :signup_helper())
    sub_btn.place(relx=0.5, rely=0.5, anchor="center")
    signup.mainloop()

def firstWindow():
    """
    sign in or sign up

    :return: null
    """


    print("im here")

    wel_label = tk.Label(root, text='Welcome to our store ', font=('calibre', 20, 'bold'))
    wel_label.place(relx=0.5, rely=0.1, anchor="center")
    in_btn = tk.Button(root, text='Sign in ', font=('calibre', 15, 'bold'), command=lambda: signinwindow())
    in_btn.place(relx=0.5, rely=0.4, anchor="center")
    up_btn = tk.Button(root, text='Sign up', font=('calibre', 15, 'bold'), command=lambda: signupwindow())
    up_btn.place(relx=0.5, rely=0.6, anchor="center")






counter=2
root = tk.Tk()

root.title('Store Storage')
window_height = 306
window_width = 612

my_img=ImageTk.PhotoImage(Image.open("istockphoto-1157106624-612x612.png"))
my_label=tk.Label(root,image=my_img)
my_label.pack()
center_screen(root)
firstWindow()
#sign_in()

root.mainloop()