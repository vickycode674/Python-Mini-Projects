from tkinter import * #graphics
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 3)) + 'Mbps'
    up  = str(round(sp.upload() / (10**6), 3)) + 'Mbps'

    lab_down.config(text=down)
    lab_up.config(text=up)





sp = Tk()

sp.title("Internet Speed Test")
sp.geometry("400x650")
sp.config(bg="blue")

lab = Label(sp,text="Internet Speed Test",font=("Time New Roman",30,"bold"))
lab.place(x=80,y=40,height=50,width=340)

lab = Label(sp,text="Downloading Speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=130,height=50,width=380)

lab_down = Label(sp,text="00",font=("Time New Roman",30,"bold"),bg="blue",fg="white")
lab_down.place(x=60,y=200,height=30,width=380)

lab = Label(sp,text="Uploading Speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

lab_up = Label(sp,text="00",font=("Time New Roman",30,"bold"),bg="blue",fg="white")
lab_up.place(x=60,y=360,height=30,width=380)

button = Button(sp,text="Check Speed",font=("Times New Roman",30,"bold"),relief=RAISED,bg="red",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)




sp.mainloop()