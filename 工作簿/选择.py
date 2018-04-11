# coding = utf-8

import tkinter
import tkinter.messagebox
import tkinter.ttk

root = tkinter.Tk()
root.title('Selection widgets')
root['height'] = 400
root['width'] = 320
root.resizable(False, False)

varName = tkinter.StringVar()
varName.set('')


labelGrade = tkinter.Label(root, text='Grade', justify=tkinter.RIGHT, width=50)
labelGrade.place(x=10, y=40, width=50, height=20)
studentClasses = {'1': ['1', '2', '3', '4'],
                  '2': ['1', '2'],
                  '3': ['1', '2', '3']}
comboGrade = tkinter.ttk.Combobox(root, width=50, value=tuple(studentClasses.keys()))
comboGrade.place(x=70, y=40, width=50, height=20)

def comboChange(event):
    grade = comboGrade.get()
    if grade:
        comboClass['values'] = studentClasses.get(grade)
    else:
        comboClass.set([])


comboGrade.bind('<<ComboboxSelected>>', comboChange)

labelClass = tkinter.Label(root, text='Class', justify=tkinter.RIGHT, width=50)
labelClass.place(x=130, y=40, width=40, height=20)

comboClass = tkinter.ttk.Combobox(root, width=50)
comboClass.place(x=190, y=40, width=50, height=20)

root.mainloop()
