import tkinter as tk

root=tk.Tk()
root.title("calculator")
f=tk.Frame(root, bg="gray", cursor="hand2")
f.pack()
#text_i=tk.StringVar()
inp=tk.Entry(f, bg="lightblue", font=("Arial", 15, "bold"))
inp.grid(row=0, column=0, columnspan=4)
symbols=["(", ")", "%", "/", "1", "2", "3", "*", "4", "5", "6", "-", "7", "8", "9", "+", "C", "0", ".", "="] # C, =

def submit():
    try:
        res=eval(inp.get())
        inp.delete(0, tk.END)
        inp.insert(tk.END, str(res))
    except:
        inp.delete(0, tk.END)
        inp.insert(tk.END, "Error")
def create_widget(symbol, **options):
    return tk.Button(f, text=symbol, fg="black", bg="white", font=("Arial", 20, "bold"), **options)
k=0
for r in range(1, 6):
    for c in range(0, 4):
        if symbols[k]!="=" and symbols[k]!= "C":
            x=create_widget(symbols[k], command=lambda sym=symbols[k]:inp.insert(tk.END, sym))
        elif symbols[k]=="C":
            x=create_widget(symbols[k], command=lambda:inp.delete(0, tk.END))
        else:
            x=create_widget(symbols[k], command=submit)
        x.grid(row=r, column=c, sticky="nsew")
        k+=1
        
            
root.mainloop()
