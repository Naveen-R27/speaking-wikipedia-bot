import wikipedia
import pyttsx3
import tkinter as tk 

#x=input("enter the topic u want to search: ")
#res=wikipedia.summary(x)

#li=[]
#engine=pyttsx3.init()

#engine.say(res)
#for i in res:
 #   li=res.split(" ")
  #  print(i,end="")
    
#engine.runAndWait()

#engine.say(res)
#engine.runAndWait()

root=tk.Tk()
root.geometry("650x650+10+10")
topic_var=tk.StringVar()

def submit():
    try:
        topic=topic_to.get()
    #answ=answ_to.get()

    #e1.insert(tk.END,topic)
        res=wikipedia.summary(topic,sentences=2)
        engine=pyttsx3.init()
        e2.insert(tk.END,res+"\n\n")
        engine.say(res)
        engine.runAndWait()
        topic_var.set("")
        
        res_txt=open("my_res.txt", "a+",encoding="utf-8")
        res_txt.write(res+"\n")
        l1.configure(text="SUCCESSFULLY COPIED TO THE FILE...\n :) ")
        res_txt.close()
    except wikipedia.exceptions.DisambiguationError :
        e2.insert(tk.END,"Try to search with more specific Key --> !!! ")
        
        
        
topic_label=tk.Label(root,text= 'TOPIC',font=('caliber',10,'bold'),fg="teal")    
topic_to=tk.Entry(root,bd = 5, textvariable=topic_var,font=('caliber',10,'bold'))

sub_bt=tk.Button(root,text='SUBMIT AND COPY',fg="teal",command = submit,font=('bold'))
b2=tk.Button(root,text="CLEAR",fg="teal",font=('bold'),command=lambda: e2.delete(1.0,tk.END))
b3=tk.Button(root,text="EXIT",bg="black",fg="red",command= root.destroy,font=('bold'))

root.title("SpeakEasy-->InfoBot")
root.configure(bg="plum")
topic_label.place(x=10,y=10)
topic_to.place(x=60,y=10)
e3=tk.Label(root,text= "INFO ->",fg="teal")
e3.place(x=10,y=50)
e2=tk.Text(root,bd=5)
e2.place(x=60,y=50,height=100,width=500)
sub_bt.place(x=200,y=200)
b2.place(x=450,y=200)
b3.place(x=380,y=250)
l1=tk.Label(root,text=" : ) ",bg="plum",fg="black")
l1.place(x=300,y=350)

root.mainloop()










