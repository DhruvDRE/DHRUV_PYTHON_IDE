from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess #for python editor

compiler =Tk() # main start
compiler.title("DHRUV IDE") # heading of the window

#file path
file_path=''
def set_file_path(path):
	global file_path
	file_path=path

#function before call
def run():
	#easy method but require a compiler of the pc
	#code=editor.get('1.0',END)  # to take valuefrom the given user that he has written in the text box
	#exec(code) #basic way to execute any python code , not the best way
	# hard method to get in screen
	if file_path=='':
		#prompt message in next three lines
		save_prompt= Toplevel()
		text=Label(save_prompt,text="Please Save Your Code First")
		text.pack()
		return
	command= f'python {file_path}' #sets python ide
	process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True) #open python scripts
	# process pipe to follow standard way of output in an order to communicte
	output,error=process.communicate()
	#show outpur in code output block
	code_output.insert('1.0',output) # to keep output at top use 1.0 ,to keep output down keep END
	code_output.insert('1.0',error) # to print error
	
def save_as():
	if file_path =='':
		path=asksaveasfilename(filetypes=[('Python Files','*.py')]) #type of files u need to save with extention
	else:
		path=file_path # if already open use this path
	with open(path,'w') as file:
		code=editor.get('1.0',END)
		file.write(code)
		set_file_path(path)
#open file
def open_file():
	path=askopenfilename(filetypes=[('Python Files','*.py')]) #type of files
	with open(path,'r') as file: #read content  of file ,remove previous data on the editor and show file
		code=file.read()
		editor.delete('1.0',END) #clear everything
		editor.insert('1.0',code) # write everything from file at first index
		set_file_path(path)
#menu bar
menu_bar=Menu(compiler) #menu at top of the frame
file_menu=Menu(menu_bar,tearoff=0)  #to remove the ---- in menu we set tearoff to 0
file_menu.add_command(label='Open',command=open_file) # for the command function
file_menu.add_command(label='Save',command=save_as) #
file_menu.add_command(label='Save As',command=save_as)
file_menu.add_command(label='Exit',command=exit) # to close the file 
menu_bar.add_cascade(label='File',menu=file_menu) # open in order 


run_bar=Menu(menu_bar,tearoff=0)  #to remove the ---- in menu we set tearoff t>
run_bar.add_command(label='Run',command=run) # for the command function
menu_bar.add_cascade(label='Run',menu=run_bar) # open in order 



compiler.config(menu=menu_bar) #set menu in the main frame


editor=Text() # write any text box
editor.pack() # full screen
#code output section just below the editor
code_output=Text(height=10)
code_output.pack() 

compiler.mainloop()
