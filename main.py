import tkinter as tk
import time

w=tk.Tk()
w.title("Consumed ")
#Create an Option list
options_list=["Ate","Drank"]
#Store value of selected option
value_inside=tk.StringVar(w)
# Set the default value of the variable
value_inside.set("Select an Option")
# Create the optionmenu widget and passing
# the options_list and value_inside to it.
question_menu = tk.OptionMenu(w, value_inside, *options_list)
question_menu.grid(row=2,column=2)



# Create Labels For Days of the Week
mon=tk.Label(text="Monday").grid(row=4,column=1)
tue=tk.Label(text="Tuesday").grid(row=5,column=1)
wed=tk.Label(text="Wednesday").grid(row=6,column=1)
thu=tk.Label(text="Thursday").grid(row=7,column=1)
fri=tk.Label(text="Friday").grid(row=8,column=1)
sat=tk.Label(text="Saturday").grid(row=9,column=1)
sun=tk.Label(text="Sunday").grid(row=10,column=1)
#label for name and item and action
name1=tk.Label(text="Enter Your Name").grid(row=0,column=1)
item=tk.Label(text="Enter The Drink or Food You Wish").grid(row=3,column=1)
item=tk.Label(text="Did the Person Drink or Eat it").grid(row=2,column=1)
# Add user entry widgets for amounts of items
a=tk.Entry(w)
b=tk.Entry(w)
c=tk.Entry(w)
d=tk.Entry(w)
e=tk.Entry(w)
f=tk.Entry(w)
g=tk.Entry(w)
#label for name and food/drink item
name=tk.Entry(w)
item=tk.Entry(w)
# add entry widgets to the gui (.grids must be seperate from tk.Entry  else
# it outputs NoneType)
name.grid(row=0,column=2)
item.grid(row=3,column=2)
a.grid(row=4,column=2)
b.grid(row=5,column=2)
c.grid(row=6,column=2)
d.grid(row=7,column=2)
e.grid(row=8,column=2)
f.grid(row=9,column=2)
g.grid(row=10,column=2)
#Create Event To add up values of chocolate
def calculate():
      choice = value_inside.get()
      print(choice)
#turn values of chocolate to int values
      h=int(a.get())
      i=int(b.get())
      j=int(c.get())
      k=int(d.get())
      l=int(e.get())
      m=int(f.get())
      n=int(g.get())
#add the values up
      tot=h+i+j+k+l+m+n
#Convert to string to use tk.Label
      tota=str(tot)
      name2=str(name.get())
      action2=str(choice)
      item2=str(item.get())
#Decide output based on drop down menu
      if action2 == "Ate":
            z=tk.Label(text= name2 + " Has ate:")
            z.grid(row=11,column=1)
            total=tk.Label(text=tota +" " + item2)
            total.grid(row=11,column=2)
            w.after(6000, z.destroy)
            w.after(6000, total.destroy)
      else:
            drank=tk.Label(text=name2+" Has Drank:")
            drank.grid(row=11, column=1)
            total = tk.Label(text=tota +" Cups Of " + item2  )
            total.grid(row=11, column=2)
            w.after(6000,drank.destroy)
            w.after(6000, total.destroy)

#Create a button to call back the calculate loop
B=tk.Button(text="Calculate",command=calculate,).grid(row=12,column=2)



w.mainloop()