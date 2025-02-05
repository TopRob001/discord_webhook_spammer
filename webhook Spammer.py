
## Webhook spammer by abaunda_MONSTR

from tkinter import *
root = Tk()
import discord_webhook
def bro():
    print("bro??")
    url = entry2.get()
    webhook1 = discord_webhook.DiscordWebhook(url=url, content=entry4.get())
    webhook1.execute()
frame = Frame(root, width=100, height=100)
button = Button(frame, width=30, height=10, text="Send", command=bro)
frame.pack()
label = Label(frame, width=40, height=2, text="Put webhook down")
entry = Entry(frame, width=40)
label.pack()
entry2 = Entry(frame, width=40)
entry2.pack()
label2 = Label(frame, width=40, height=2, text="Put message here:")
entry4 = Entry(frame, width=40)
label2.pack()
entry4.pack()
button.pack()
root.geometry("640x640")
root.title("Spammer 3000 ")

root.mainloop()