"""
Function:sign in and sign up storage store using class and csv file
Date:13/9/2022
authors:mariam& rowan & zeina



"""

import verify as v
import items as it
import pandas as pd

from tkinter import filedialog


def read_list(line_index, file_name):
    """
    read list of items
    line_index: index of the row which has tha data
    file_name: name of the file


    """

    df = pd.read_csv(file_name)
    print(line_index)
    v = df.iloc[line_index]
    dictionary = {}
    column_headers = list(df.columns.values)
    new = {column_headers[1]: df.iloc[line_index, 1], column_headers[2]: df.iloc[line_index, 2],
           column_headers[3]: df.iloc[line_index, 3], column_headers[4]: df.iloc[line_index, 4],
           column_headers[5]: df.iloc[line_index, 5],column_headers[6]: df.iloc[line_index, 6]}
    dictionary.update(new)
    obj11 = it.item(dictionary, line_index)

    return obj11


# In[3]:

def show_list(line_index, file_name):
    obj1 = read_list(line_index, "data.csv")
    return obj1.getlist(),obj1;

def access_admin(line_index, file_name):
    """
    edit list of items
    :return: none
    """
    obj1 = read_list(line_index, "data.csv")
    obj1.getlist();


    # print(list)
    x = int(input("1-set\n2-get\n"))
    if x == 1:
        obj1.set_()


    #  update_file(line.strip('\n').split(' ')[0],line.strip('\n').split(' ')[1],file_name,line_index,list)
    elif x == 2:
        obj1.get()
    # update_file(line.strip('\n').split(' ')[0],line.strip('\n').split(' ')[1],file_name,line_index,list)

    else:
        print("Please enter one of the provided options")


# In[ ]:


#email = input("email   :")
#if v.valid_email(email):


#    found, line, line_index = v.check_email(email, "t.txt")
#    print(line)
#    print(line_index)

#    if found:
#        pass_f = line.strip('\n').split(' ')[1]
#        if (v.verify_password(pass_f)):
#            access_admin(line_index, "data.csv")


#    else:
#        x = int(input("Please enter 1 if you would like to sign up:"))
#        if x == 1:
#            password = input("Please enter your password")
#            v.sign_up(email, password, "t.txt")







