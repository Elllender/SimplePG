import secrets
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from pyperclip import copy

lowercase = list(ascii_lowercase)
uppercase = list(ascii_uppercase)
digitsa = list(digits)
punctuationa = list(punctuation)

csprng = secrets.SystemRandom()


def generatepassword(length=11, l=True, u=True, d=True, p=True, ludp=None):

    struct = ''
    passwd = ''

    for flag in [(l, 'l'), (u, 'u'), (d, 'd'), (p, 'p')]:
        match flag:
            case (True, ch): struct += ch
            case (False, _): pass

    struct_list = list(struct)
    rstruct = []

    while set(struct_list) != set(rstruct):

        rstruct.clear()

        for i in range(0, length):
            rstruct.append(csprng.choice(struct_list))

    csprng.shuffle(rstruct)

    for i in range(0, len(rstruct)):
        match rstruct[i]:
            case 'l': passwd += csprng.choice(ludp[0])
            case 'u': passwd += csprng.choice(ludp[1])
            case 'd': passwd += csprng.choice(ludp[2])
            case 'p': passwd += csprng.choice(ludp[3])

    return passwd


def copypass():
    copy(cpass.get())
    showinfo('Copied', "Copied !")


def generate():
    cbss = [checkbutton_lowercase_var.get(), checkbutton_uppercase_var.get(), checkbutton_digit_var.get(), checkbutton_punctuation_var.get()]
    cbss = [True if x == 1 else False for x in cbss]

    ludp = [entry_lowercase_var.get(), entry_uppercase_var.get(), entry_digits_var.get(), entry_punctuation_var.get()]
    cpass.set(generatepassword(length=length_var.get(), l=cbss[0], u=cbss[1], d=cbss[2], p=cbss[3], ludp=ludp))


def checkbutton_lowercase():
    if checkbutton_lowercase_var.get() == 1:
        entry_lowercase_after['state'] = ACTIVE
    else:
        entry_lowercase_after['state'] = DISABLED


def checkbutton_uppercase():
    if checkbutton_uppercase_var.get() == 1:
        entry_uppercase_after['state'] = ACTIVE
    else:
        entry_uppercase_after['state'] = DISABLED


def checkbutton_digits():
    if checkbutton_digit_var.get() == 1:
        entry_digits_after['state'] = ACTIVE
    else:
        entry_digits_after['state'] = DISABLED


def checkbutton_special():
    if checkbutton_punctuation_var.get() == 1:
        entry_punctuation_after['state'] = ACTIVE
    else:
        entry_punctuation_after['state'] = DISABLED


root = Tk()

root.title('CSPG')
root.geometry("495x250")

cpass = StringVar(value="| ----------------- |") # generatepassword(length=32)
length_var = IntVar()

style = ttk.Style()
style.theme_use('clam')
style.configure("M.TButton", font=('Verdana', 10, 'normal'), relief="groove", padding=1, background='#eeeeee')
style.configure("M.TFrame", background='Gainsboro')
style.configure("M.TCheckbutton", font=('Verdana', 10, 'normal'), background='Gainsboro')

for c in range(2): root.grid_columnconfigure(index=c, weight=1)
for c in range(3): root.grid_rowconfigure(index=c, weight=1)


# frame 0
frame0 = ttk.Frame(root, borderwidth=2, relief='groove') #flat, groove, raised, ridge, solid, or sunken
frame0.grid(column=0, row=0, sticky=NSEW, pady=3, padx=7, columnspan=2)

for c in range(1): frame0.grid_columnconfigure(index=c, weight=1)
for c in range(1): frame0.grid_rowconfigure(index=c, weight=1)
# frame 0

# frame 1
frame1 = ttk.Frame(root, borderwidth=2, relief='groove') #flat, groove, raised, ridge, solid, or sunken
frame1.grid(column=0, row=1, sticky=NSEW, pady=3, padx=7)

for c in range(2): frame1.grid_columnconfigure(index=c, weight=1)
for c in range(2): frame1.grid_rowconfigure(index=c, weight=1)
# frame 1

# frame 2
frame2 = ttk.Frame(root, borderwidth=2, relief='groove') #flat, groove, raised, ridge, solid, or sunken
frame2.grid(column=0, row=2, sticky=NSEW, pady=3, padx=7, columnspan=2)

for c in range(2): frame2.grid_columnconfigure(index=c, weight=1)
for c in range(4): frame2.grid_rowconfigure(index=c, weight=1)
# frame 2

# frame 3
frame3 = ttk.Frame(root, borderwidth=2, relief='groove') #flat, groove, raised, ridge, solid, or sunken
frame3.grid(column=1, row=1, sticky=NSEW, pady=3, padx=7)

for c in range(1): frame3.grid_columnconfigure(index=c, weight=1)
for c in range(1): frame3.grid_rowconfigure(index=c, weight=1)
# frame 3

label = ttk.Label(frame0, textvariable=cpass, font=('Verdana', 12, 'normal'), background='Gainsboro')
label.grid(column=0, row=0)

button_generate = ttk.Button(frame1, text='Generate', style="M.TButton", takefocus=0, command=generate, width=12, padding=3)
button_generate.grid(column=0, row=0, rowspan=2)

button_copy = ttk.Button(frame1, text='Copy', style="M.TButton", takefocus=0, command=copypass, width=12, padding=3)
button_copy.grid(column=1, row=0, rowspan=2)

label_length = ttk.Label(frame3, text='Length', font=('Verdana', 10, 'bold'))
label_length.grid(column=0, row=0)

length_var.set(4)
spinbox_length = ttk.Spinbox(frame3, from_=4, to=32, textvariable=length_var, wrap=True, state='readonly', width=2, font=('Consolas', 12))
spinbox_length.grid(column=1, row=0, padx=8)

checkbutton_lowercase_var = IntVar(value=1)
checkbutton_uppercase_var = IntVar(value=1)
checkbutton_digit_var = IntVar(value=1)
checkbutton_punctuation_var = IntVar(value=1)

checkbutton_lowercase = ttk.Checkbutton(frame2, text='Lowercase', style='M.TCheckbutton', takefocus=0, variable=checkbutton_lowercase_var, command=checkbutton_lowercase)
checkbutton_lowercase.grid(column=0, row=0, sticky=W, padx=8, pady=5)

checkbutton_uppercase = ttk.Checkbutton(frame2, text='Uppercase', style='M.TCheckbutton', takefocus=0, variable=checkbutton_uppercase_var, command=checkbutton_uppercase)
checkbutton_uppercase.grid(column=0, row=1, sticky=W, padx=8, pady=5)

checkbutton_digit = ttk.Checkbutton(frame2, text='Digits', style='M.TCheckbutton', takefocus=0, variable=checkbutton_digit_var, command=checkbutton_digits)
checkbutton_digit.grid(column=0, row=2, sticky=W, padx=8, pady=5)

checkbutton_punctuation = ttk.Checkbutton(frame2, text='Special', style='M.TCheckbutton', takefocus=0, variable=checkbutton_punctuation_var, command=checkbutton_special)
checkbutton_punctuation.grid(column=0, row=3, sticky=W, padx=8, pady=5)

entry_lowercase_var = StringVar(value=ascii_lowercase)
entry_uppercase_var = StringVar(value=ascii_uppercase)
entry_digits_var = StringVar(value=digits)
entry_punctuation_var = StringVar(value=punctuation)

entry_lowercase_after = ttk.Entry(frame2, textvariable=entry_lowercase_var, font=('Verdana', 10, 'normal'), takefocus=0, justify=CENTER)
entry_lowercase_after.grid(column=1, row=0, sticky=EW, padx=7, pady=5)

entry_uppercase_after = ttk.Entry(frame2, textvariable=entry_uppercase_var, font=('Verdana', 10, 'normal'), takefocus=0, justify=CENTER)
entry_uppercase_after.grid(column=1, row=1, sticky=EW, padx=7, pady=5)

entry_digits_after = ttk.Entry(frame2, textvariable=entry_digits_var, font=('Verdana', 10, 'normal'), takefocus=0, justify=CENTER)
entry_digits_after.grid(column=1, row=2, sticky=EW, padx=7, pady=5)

entry_punctuation_after = ttk.Entry(frame2, textvariable=entry_punctuation_var, font=('Verdana', 10, 'normal'), takefocus=0, justify=CENTER)
entry_punctuation_after.grid(column=1, row=3, sticky=EW, padx=7, pady=5)

root.attributes('-toolwindow', True)
root.resizable(False, False)
root.mainloop()