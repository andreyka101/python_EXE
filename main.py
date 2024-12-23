# from num import arr
# print(arr)
# print("hello")
# input("===")







from tkinter import *
from tkinter import ttk
window = Tk()
window.title("window")
window.geometry("600x500")
window.config(bg="#facca6")
def fun_1():
    if(numbers.get() == "b1"):
        window.configure( bg = "#ff1c1c")
    if(numbers.get() == "b2"):
        window.configure( bg = "#ffd500")
    if(numbers.get() == "b3"):
        window.configure( bg = "#51ff00")
numbers = StringVar(value="b1")
but_1 = ttk.Radiobutton(text="123" , value= "b1" , variable= numbers , command=fun_1)
but_1.place(x=10 , y=10)
but_2 = ttk.Radiobutton(text="456" , value= "b2" , variable= numbers , command=fun_1)
but_2.place(x=10 , y=40)
but_3 = ttk.Radiobutton(text="789" , value= "b3" , variable= numbers , command=fun_1)
but_3.place(x=10 , y=70)
window.mainloop()
