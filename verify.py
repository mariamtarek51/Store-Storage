"""
Function:QuadroZona emails
Version:V1
Author:Rowan & Mariam & Khaled
Date:12/9/2022
"""
import csv

def check_email(email, File):
    """
    check whether email in the file or not
    :param email: entered email
    :param File: name of the text file
    :return: Whther is found or not, saved password
    """

    with open(File, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if line.find(email) != -1:
                print("Email found")

                return True, line, lines.index(line)
        print("Email not found")
        return False, -1, -1


def valid_email(email):
    """
    check if it's a valid email
    :param email:entered email
    :return: boolean if it's valid or not
    """
    print("email in valid",email)
    result = email.endswith('@qz.com')
    if result:
        print("valid email")
        return True
    else:
        print("invalid emai nol")
        return False


def verify_password(pass_f,entered_Pass):
    """
    checks if entered password matches email
    :param pass_f: Saved password
    :return: boolean if the password is correct or not
    """
    if entered_Pass == pass_f:
        print("Password is correct")
        return True
    else:
        print("Password incorrect\n")
        return False











  #  counter = 3
   # while (counter):
    #    #password = input("Please enter your password:")
     #   if entered_Pass == pass_f:
      #      print("Password is correct")
       #     return True

        #else:
         #   counter = counter - 1
          #  print("Password incorrect\n")
           # return False








def sign_up(email, password, file_nametxt,filenamecsv):
    """
    sign up
    :param email:entered email
    :param password:entered password
    :return:none
    """
    str = "\n" + email + ' ' + password
    with open(file_nametxt, 'a') as fp:
        fp.write(str)
    dict = {"user_name":email, "milk": "0", "apple": "0", "juice": "0", "Water": "0","grapes":"0","oranges":"0"}
    field_names = ['user_name', 'milk', 'apple', 'juice', 'Water','grapes','oranges']

    with open(filenamecsv, 'a') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names)

        dict_object.writerow(dict)


