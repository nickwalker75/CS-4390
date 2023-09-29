import yagmail
import os

print("      Nick's Email Service")
print("-----------------------------------")

cwd = os.getcwd()
pwrd = "skkaxfdxotzocows"
user = "nickrocks75@gmail.com"

# enter email info
receiver = input("Enter reciver email: ")
subject = input("Enter Subject: ")
emailMsg = input("Enter Message: ")

# check for attachment
flag = input("Attach Image File?(y/n): ")
if(flag == 'y' or flag == 'Y'):
    fName = input("Enter File Name(incl. file ext.): ")

contents = [emailMsg, yagmail.inline("{0}\{1}".format(cwd, fName))]

# login and send email
try:
    yag = yagmail.SMTP(user, pwrd)
    yag.send(receiver, subject, contents)
    print("Email Sent!")
except:
    print("Error, Email was not sent")
