import customtkinter as ctk
import tkinter as tk


def click(text):
    global value
    if text == "=":
        try:
            result = str(eval(value.get()))  
            value.set(result)
        except:
            value.set("Error")
    elif text == "C":
        value.set("")
    elif text == "AC":
        current_value = value.get()
        value.set(current_value[:-1])
    elif text == "x²":
        try:
            num = float(eval(value.get()))
            result = str(num ** 2)
            value.set(result)
        except:
            value.set("Error")
    elif text == "%":
        try:
            num = float(eval(value.get()))
            result = str(num / 100)
            value.set(result)
        except:
            value.set("Error")    
    else:
        value.set(value.get() + text)  

    



root = ctk.CTk()

root.geometry("470x450")
root.title("Simple Calculator")

value = tk.StringVar()
value.set("")

display = ctk.CTkEntry(root,height=80,width=450,text_color="white",fg_color="gray20",font=('lucida', 25 ,'bold'),textvariable=value)
display.place(x=10,y=10)


button = ctk.CTkButton(root,text="9",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("9"))
button.place(x=35,y=130)
button = ctk.CTkButton(root,text="8",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("8"))
button.place(x=135,y=130)
button = ctk.CTkButton(root,text="7",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("7"))
button.place(x=235,y=130)
button = ctk.CTkButton(root,text="x",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("*"))
button.place(x=335,y=130)

button = ctk.CTkButton(root,text="6",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("6"))
button.place(x=35,y=180)
button = ctk.CTkButton(root,text="5",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("5"))
button.place(x=135,y=180)
button = ctk.CTkButton(root,text="4",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("4"))
button.place(x=235,y=180)
button = ctk.CTkButton(root,text="÷",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("/"))
button.place(x=335,y=180)

button = ctk.CTkButton(root,text="3",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("3"))
button.place(x=35,y=230)
button = ctk.CTkButton(root,text="2",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("2"))
button.place(x=135,y=230)
button = ctk.CTkButton(root,text="1",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("1"))
button.place(x=235,y=230)
button = ctk.CTkButton(root,text="+",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("+"))
button.place(x=335,y=230)

button = ctk.CTkButton(root,text="0",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("0"))
button.place(x=35,y=280)
button = ctk.CTkButton(root,text="00",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("00"))
button.place(x=135,y=280)
button = ctk.CTkButton(root,text="000",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("000"))
button.place(x=235,y=280)
button = ctk.CTkButton(root,text="-",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("-"))
button.place(x=335,y=280)

button = ctk.CTkButton(root,text="(",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("("))
button.place(x=35,y=330)
button = ctk.CTkButton(root,text=")",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click(")"))
button.place(x=135,y=330)
button = ctk.CTkButton(root,text=".",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("."))
button.place(x=235,y=330)
button = ctk.CTkButton(root,text="%",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("%"))
button.place(x=335,y=330)

button = ctk.CTkButton(root,text="AC",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("AC"))
button.place(x=35,y=380)
button = ctk.CTkButton(root,text="C",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("C"))
button.place(x=135,y=380)
button = ctk.CTkButton(root,text="x²",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("**2"))
button.place(x=235,y=380)
button = ctk.CTkButton(root,text="=",text_color="black",fg_color="white",width=90,font=('lucida', 20 ,'bold'), command=lambda: click("="))
button.place(x=335,y=380)




root.mainloop()