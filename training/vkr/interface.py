import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

window = tk.Tk()
icon = tk.PhotoImage(file = 'images.png')
window.iconphoto(False, icon)
window.title('Welding part')
window.geometry('1024x640')
window.resizable(False, False)
window.config(bg='White')

tabControl = ttk.Notebook(window, padding=(25,0,25,100))
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Welding')

lb1_tab1 = Label(tab1, text='Equipment coordinates', font='Helvetica 18')
lb1_tab1.place(x=20, y=20)

lbtx_tab1 = Label(tab1, text='X:', font='Helvetica 14')
lbtx_tab1.place(x=20, y=60)
lbx_tab1 = Label(tab1, text=0, font='Helvetica 14', bg = 'White')
lbx_tab1.place(x=40, y=60)
lbty_tab1 = Label(tab1, text='Y:', font='Helvetica 14')
lbty_tab1.place(x=20, y=90)
lby_tab1 = Label(tab1, text=0, font='Helvetica 14', bg = 'White')
lby_tab1.place(x=40, y=90)
lbtz_tab1 = Label(tab1, text='Z:', font='Helvetica 14')
lbtz_tab1.place(x=20, y=120)
lbz_tab1 = Label(tab1, text=0, font='Helvetica 14', bg = 'White')
lbz_tab1.place(x=40, y=120)

btn_xyz = Button(tab1, text='Reset', bg='White', bd = '5', padx=50)
btn_xyz.place(x=20, y=160)

lb_input_parameter_tab1 = Label(tab1, text='Input welding parameter', font='Helvetica 18')
lb_input_parameter_tab1.place(x=20, y=220)

lb_metall_tab1 = Label(tab1, text='Material:', font='Helvetica 14')
lb_metall_tab1.place(x=20, y=260)

ch_met = IntVar(value=0)
metal1_rb = Radiobutton(tab1,text='Steel',font='Helvetica 14', variable=ch_met, value = 0)
metal1_rb.place(x=100,y=260)
metal2_rb = Radiobutton(tab1,text='Aluminum',font='Helvetica 14', variable=ch_met, value = 1)
metal2_rb.place(x=200,y=260)

lb_parm1_tab1 = Label(tab1, text='Part tickness, (mm):', font='Helvetica 14')
lb_parm1_tab1.place(x=20, y=300)

parm1 = Combobox(tab1, values=(0, 1, 2), state='readonly')
parm1.current(0)
parm1.place(x=325,y=305)

lb_parm2_tab1 = Label(tab1, text='Amperage value, (kA):', font='Helvetica 14')
lb_parm2_tab1.place(x=20, y=330)
lb_parm3_tab1 = Label(tab1, text='Welding time, (sec):', font='Helvetica 14')
lb_parm3_tab1.place(x=20, y=360)
lb_parm4_tab1 = Label(tab1, text='Electrode compression force, (kN):', font='Helvetica 14')
lb_parm4_tab1.place(x=20, y=390)

val_parm2 = Combobox(tab1, values=(0, 7.5, 10.5, 24, 30), state='readonly')
val_parm2.current(0)
val_parm2.place(x=325, y=335)
val_parm3 = Combobox(tab1, values=(0, 0.4,0.6,0.12,0.18), state='readonly')
val_parm3.current(0)
val_parm3.place(x=325, y=365)
val_parm4 = Combobox(tab1, values=(0, 1.5, 3.5, 4, 7), state='readonly')
val_parm4.current(0)
val_parm4.place(x=325, y=395)

btn_set = Button(tab1, text='Set', bg='White', bd = '5', padx=50)
btn_set.place(x=20, y=430)

lb_welres1_tab1 = Label(tab1, text='Location process result:', font='Helvetica 18')
lb_welres1_tab1.place(x=600, y=20)
welres1_tab1 = Label(tab1, text='Unknown', font='Helvetica 14',bg='White', fg = 'Black')
welres1_tab1.place(x=600, y=50)

lb_welres2_tab1 = Label(tab1, text='Welding process result:', font='Helvetica 18')
lb_welres2_tab1.place(x=600, y=100)
welres2_tab1 = Label(tab1, text='Unknown', font='Helvetica 14', bg='White', fg = 'Black')
welres2_tab1.place(x=600, y=130)

lb_welres3_tab1 = Label(tab1, text='Process status:', font='Helvetica 18')
lb_welres3_tab1.place(x=600, y=180)
welres3_tab1 = Label(tab1, text='Stop', font='Helvetica 14', bg='White',fg= 'Darkred')
welres3_tab1.place(x=600, y=210)

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text ='Control')

lb_param1_tab2 = Label(tab2, text='Specified product parameters', font='Helvetica 18')
lb_param1_tab2.place(x=20, y=20)

paramw1 = Label(tab2, text='Width, (mm):', font='Helvetica 14')
paramw1.place(x=20, y=60)
paraml1 = Label(tab2, text='Length, (mm):', font='Helvetica 14')
paraml1.place(x=20, y=90)
paramh1 = Label(tab2, text='Height, (mm):', font='Helvetica 14')
paramh1.place(x=20, y=120)
paramh1 = Label(tab2, text='Model name:', font='Helvetica 14')
paramh1.place(x=20, y=150)

param_var1 = IntVar(value=0)
param_var2 = IntVar(value=0)
param_var3 = IntVar(value=0)
param_var4 = StringVar(value='Input model')
paramw_ipt = Entry(tab2,width=20, relief=SUNKEN, bd = 3, textvariable=param_var1)
paramw_ipt.place(x=150, y=64)
paraml_ipt = Entry(tab2,width=20, relief=SUNKEN, bd = 3, textvariable=param_var2)
paraml_ipt.place(x=150, y=94)
paramh_ipt = Entry(tab2,width=20, relief=SUNKEN, bd = 3, textvariable=param_var3)
paramh_ipt.place(x=150, y=124)
paramm_ipt = Entry(tab2,width=20, relief=SUNKEN, bd = 3, textvariable=param_var4)
paramm_ipt.place(x=150, y=154)

btn_set_param = Button(tab2, text='Set', bg='White', bd = '5', padx=50)
btn_set_param.place(x=20, y=190)

lb_param1_tab2 = Label(tab2, text='Current product parameters', font='Helvetica 18')
lb_param1_tab2.place(x=20, y=250)

paramw2 = Label(tab2, text='Width, (mm):', font='Helvetica 14')
paramw2.place(x=20, y=290)
paraml2 = Label(tab2, text='Length, (mm):', font='Helvetica 14')
paraml2.place(x=20, y=320)
paramh2 = Label(tab2, text='Height, (mm):', font='Helvetica 14')
paramh2.place(x=20, y=350)

paramw_cpt = Label(tab2,text=0, font='Helvetica 14', bg = 'White')
paramw_cpt.place(x=150, y=294)
paraml_cpt = Label(tab2,text=0, font='Helvetica 14', bg = 'White')
paraml_cpt.place(x=150, y=324)
paramh_cpt = Label(tab2,text=0, font='Helvetica 14', bg = 'White')
paramh_cpt.place(x=150, y=354)

ctrl_res = Label(tab2,text='Control process result:', font='Helvetica 18')
ctrl_res.place(x=600, y=20)
ctrl_res1 = Label(tab2,text='Unknown', font='Helvetica 14', bg = 'White', fg='Black')
ctrl_res1.place(x=600, y=50)

ctrl_sts = Label(tab2,text='Control process status:', font='Helvetica 18')
ctrl_sts.place(x=600, y=100)
ctrl_sts1 = Label(tab2,text='Unknown', font='Helvetica 14', bg = 'White', fg='Black')
ctrl_sts1.place(x=600, y=130)

cur_qnt = Label(tab2,text='Current quantity of products:', font='Helvetica 18')
cur_qnt.place(x=600, y=180)
cur_qnt1 = Label(tab2,text='Success:', font='Helvetica 14',fg= 'Darkgreen')
cur_qnt1.place(x=600, y=210)
cur_qnt2 = Label(tab2,text='Unsuccess:', font='Helvetica 14',fg= 'Darkred')
cur_qnt2.place(x=600, y=240)

cur_qnt_res1 = Label(tab2,text=0, font='Helvetica 14', bg = 'White')
cur_qnt_res1.place(x=710, y=210)
cur_qnt_res2 = Label(tab2,text=0, font='Helvetica 14', bg = 'White')
cur_qnt_res2.place(x=710, y=240)


btn_str = Button(window, text='Start', bg='White', bd = '5', padx=50)
btn_str.place(x=20, y=550)
btn_stp = Button(window, text='Stop', bg='White', bd = '5', padx=50)
btn_stp.place(x=170, y=550)

tabControl.pack(expand=1, fill='both')
window.mainloop()