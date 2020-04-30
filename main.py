import requests
from tkinter import *
from tkinter.messagebox import showinfo, showerror

#  function for  sending sms for number
def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization' : '<APIKEY-Provide By Fast2SMS>',
        'sender_id' : 'FSTSMS',
        'message' : message,
        'language' : 'english',
        'route' : 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)


# call function on click button
def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    req = send_sms(num, msg)

    if(req == True):
        showinfo("Send Success", "SMS Send Successfully!")
    else:
        showerror("Sending failed", "SMS Sending failed?")

#  UI for sending sms
root = Tk()
root.title("Message Sender !")
root.geometry("400x490")
root.minsize(400,490)
root.maxsize(400,490)
font = ('Helvetica', 22, 'bold')
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=15)
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root, text="Send SMS", command=btn_click)
sendBtn.pack()
root.mainloop()
