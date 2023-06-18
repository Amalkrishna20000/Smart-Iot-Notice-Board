import os
import requests
from tkinter import Tk, Button

if os.environ.get('DISPLAY', '') == '':
    print('No display found. Using :0.0')
    os.environ.setdefault('DISPLAY', ':0.0')

ip = input("Please enter the IP address: ")

root = Tk()
root.geometry("400x200")

def send_request():
    try:
        requests.get("http://" + ip + "/set-status-accept/")
        print(requests.get("http://" + ip + "/get-status/").text)
    except requests.exceptions.RequestException as e:
        print(e)

def reject_request():
    try:
        requests.get("http://" + ip + "/set-status-reject/")
        print(requests.get("http://" + ip + "/get-status/").text)
    except requests.exceptions.RequestException as e:
        print(e)

def exit_application():
    root.destroy()

new_btn = Button(root, text='New Message', bd='8', command=send_request)
rec_btn = Button(root, text='Message Received', bd='8', command=send_request)
accept_btn = Button(root, text='Accept', bd='8', command=send_request)
reject_btn = Button(root, text='Reject', bd='8', command=reject_request)
exit_btn = Button(root, text='Exit', bd='8', command=exit_application)

new_btn.place(x=30, y=30)
rec_btn.place(x=150, y=30)
accept_btn.place(x=30, y=80)
reject_btn.place(x=150, y=80)
exit_btn.place(x=90, y=140)

root.mainloop()
