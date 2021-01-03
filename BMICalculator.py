from tkinter import *

root = Tk()
root.title("BMI Calculator")
root.geometry("302x500")
#root.iconbitmap(r'BMICalcIcon.ico')
root.resizable(False, False)
ans = Label(root)

def calculate():
    global ans
    ans.destroy()
    Value_1=height_slider.get()
    Value_2=weight_slider.get()
    con_val = (Value_1 / 12)
    con_val2 = (con_val / 3.2808)
    bmi = (Value_2 / (con_val2**2))
    ans = Label(root, text=bmi, font=("arial", 10, "bold"), bg="#ffffff")
    ans.grid(row=7, column=0)

title_BMI = Label(root, text="BMI Calculator", font=("arial", 20, "bold"), bg="#ffffff").grid(row=1, column=0)
height_init = Label(root, text="Enter your Height in Inches: ", font=("arial", 10, "bold"), bg="#ffffff").grid(row=2, column=0)
height_slider = Scale(root, orient = HORIZONTAL, from_=0, to=100, resolution=1, length= 301, bg="#ffffff")
height_slider.grid(row=3, column=0)
weight_init = Label(root, text="Enter your weight in KGs: ", font=("arial", 10, "bold"), bg="#ffffff").grid(row=4, column=0)
weight_slider = Scale(root, orient = HORIZONTAL, length= 301, bg="#ffffff")
weight_slider.grid(row=5, column=0)

calc_btn = Button(root, text="Calculate", font=("arial", 10, "bold"), bg="#ffffff", command=calculate).grid(row= 6, column=0)

title_index = Label(root, text="BMI Index", relief=RIDGE, font=("arial", 18, "bold"), bg="#ffffff").grid(row=8, column=0, pady= 8) 

index1 = Label(root, text=">18.5 = Underweight", font=("arial", 10, "bold"), bg="#ffffff").grid(row=9, column=0, pady=5)
index2 = Label(root, text="18.5-24.9 = Ideal", font=("arial", 10, "bold"), bg="#ffffff").grid(row=10, column=0, pady=5)
index3 = Label(root, text="25-29.9 = Over weight", font=("arial", 10, "bold"), bg="#ffffff").grid(row=11, column=0, pady=5)
index4 = Label(root, text="30-34.9 = Obesity I", font=("arial", 10, "bold"), bg="#ffffff").grid(row=12, column=0, pady=5)
index5 = Label(root, text="35-39.9 = Obesity II", font=("arial", 10, "bold"), bg="#ffffff").grid(row=13, column=0, pady=5)
index6 = Label(root, text=">40 = Obesity III, Death risk", font=("arial", 10, "bold"), bg="#ffffff").grid(row=14, column=0, pady=5)

end_writing = Label(root, text="Made by Arib Muhtasim", font=("arial", 10, "bold"), bg="black", fg="#ffffff", relief=SUNKEN).grid(row = 15, column=0, padx=6, pady=6)

root.configure(background = "#ffffff")
root.mainloop()