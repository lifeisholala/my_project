import tkinter



a_a = 0
a_b = 0
a_c = 0
b_a = 0
b_b = 0
b_c = 0
c_a = 0
c_b = 0
c_c = 0

window = tkinter.Tk()
window.title("tictakto")
window.geometry('275x275+550+300')

def F_f():
    pass





button_1_1 = tkinter.Button(bg='black',height=5,width=6)
button_1_2 = tkinter.Button(bg='black',height=5,width=6)
button_1_3 = tkinter.Button(bg='black',height=5,width=6)
button_2_1 = tkinter.Button(bg='black',height=5,width=6)
button_2_2 = tkinter.Button(bg='black',height=5,width=6)
button_2_3 = tkinter.Button(bg='black',height=5,width=6)
button_3_1 = tkinter.Button(bg='black',height=5,width=6)
button_3_2 = tkinter.Button(bg='black',height=5,width=6)
button_3_3 = tkinter.Button(bg='black',height=5,width=6)

button_1_1.grid(row=0,column=0)
button_1_2.grid(row=0,column=1)
button_1_3.grid(row=0,column=2)
button_2_1.grid(row=1,column=0)
button_2_2.grid(row=1,column=1)
button_2_3.grid(row=1,column=2)
button_3_1.grid(row=2,column=0) 
button_3_2.grid(row=2,column=1)
button_3_3.grid(row=2,column=2)














window.mainloop()