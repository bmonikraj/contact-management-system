#DBMS PROJECT development part in Python 2.7 along with integrating Database MySQL 5.6
#Author - Monik Raj Behera
#Roll Number - 114cs0095
#Subject Code - CS-222
#Programming Language : Python(2.7)
#Database Management system : MySQL(5.6)
#Description - This is a project which is focused to develop an application with Graphical User Interface and also platform independent which can help the client in
#managing his/her contacts and details.
#
#Two Databases are created:
'''
1. Database with attributes Name, Contact , E-mail ID, Date of creation , ID-Number
2. Database with attribute Name, Address, ID-Number
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


from Tkinter import *
import sys
import mysql.connector
import time
import tkMessageBox

#defining different functions in the root window

cnx = None

def add_fun():
    add_w = Toplevel()
    add_w.resizable(width = TRUE, height = FALSE)
    add_w.configure(bg = '#FFCCFF')
    add_w.title('ADDING CONTACTS')
    add_w.iconbitmap('icon.ico')
    a_name = Entry(add_w)
    a_contact = Entry(add_w)
    a_mail = Entry(add_w)
    a_address = Entry(add_w)
    a_date = Entry(add_w)
    a_id = Entry(add_w)
    a_gn = Entry(add_w)
    a_na_l = Label(add_w , text = 'Enter Name')
    a_na_l.configure(bg = '#E68AB8')
    a_con_l = Label(add_w , text = 'Enter Contact No')
    a_con_l.configure(bg = '#E68AB8')
    a_mail_l = Label(add_w , text = 'Enter mail Id')
    a_mail_l.configure(bg = '#E68AB8')
    a_adr_l = Label(add_w, text = 'Enter address')
    a_adr_l.configure(bg = '#E68AB8')
    a_dat_l = Label(add_w , text = 'Enter the date of Creation(YYYY-MM-DD)')
    a_dat_l.configure(bg='#E68AB8')
    a_id_l =Label(add_w , text = 'Enter ID no')
    a_id_l.configure(bg = '#E68AB8')
    a_na_l.grid(row = 0, column = 0)
    a_con_l.grid(row = 1 , column = 0)
    a_mail_l.grid(row = 2 , column = 0)
    a_adr_l.grid(row = 3 , column = 0)
    a_dat_l.grid(row = 4 , column = 0)
    a_id_l.grid(row = 5 , column = 0)
    a_name.grid(row = 0, column = 1)
    a_contact.grid(row = 1 , column = 1)
    a_mail.grid(row = 2 , column = 1)
    a_address.grid(row = 3 , column = 1)
    a_date.grid(row = 4 , column = 1)
    a_id.grid(row = 5 , column = 1)
    def add_exe():
        name = a_name.get()
        contact = a_contact.get()
        mail = a_mail.get()
        address = a_address.get()
        date = a_date.get()
        id = a_id.get()
        crs = cnx.cursor()                  
        #crs.execute("INSERT INTO contacts (_name, contact_no, email_id, date_created, id_no) VALUES ('" + name +"','" + contact + "','" + mail + "','" + date + "','"+ id +"')")
        #crs.execute("INSERT INTO address (_name, _address, id_no) VALUES('" + name +"','" + address + "','" + id +"')")
        try:
            crs.execute("INSERT INTO contacts (_name, contact_no, email_id, date_created, id_no) VALUES ('" + name +"','" + contact + "','" + mail + "','" + date + "','"+ id +"')")
            crs.execute("INSERT INTO address (_name, _address, id_no) VALUES('" + name +"','" + address + "','" + id +"')")
            tkMessageBox.showinfo(title = 'ADDING CONTACTS', message = 'CONTACT ADDED SUCCESSFULLY')
            crs.close()
            add_w.destroy()
        except mysql.connector.Error as e:
            root.destroy()
            tkMessageBox.showinfo(title = 'ADDING CONTACTS', message = e)
    a_ok = Button(add_w, text = 'ADD' , command = add_exe)
    a_ok.configure(relief = 'raised', fg = 'black' , bg = '#E68AB8' , bd =5)
    a_ok.grid(row = 7 , column = 1)
                  
    

def update_fun():
    update_w = Toplevel()
    update_w.resizable(width = FALSE, height = FALSE)
    update_w.configure(bg = '#FFCCFF')
    update_w.title('UPDATING CONTACTS')
    update_w.iconbitmap('icon.ico')
    def update_exe():
        ups = cnx.cursor()
        if v.get() is 1:
            ups.execute("UPDATE contacts SET _name = '" + upe2.get() + "' WHERE id_no = '" + upe1.get() + "'")
            ups.execute("UPDATE address SET _name = '" + upe2.get() + "' WHERE id_no = '" + upe1.get() + "'")
        if v.get() is 2:
            ups.execute("UPDATE contacts SET contact_no = '" + upe2.get() + "' WHERE id_no = '" + upe1.get() + "'")
        if v.get() is 3:
            ups.execute("UPDATE contacts SET email_id = '" + upe2.get() + "' WHERE id_no = '" + upe1.get() + "'")
        if v.get() is 4:
            ups.execute("UPDATE address SET _address = '" + upe2.get() + "' WHERE id_no = '" + upe1.get() + "'")
        update_w.destroy()
        ups.close()
        tkMessageBox.showinfo(title = 'UPDATE', message = 'CONTACT UPDATED SUCCESSFULLY')

    v = IntVar()
    f0 = Frame(update_w)
    f1 = Frame(update_w)
    f2 = Frame(update_w)
    f3 = Frame(update_w)
    lab = Label(f0, text = 'Choose the parameter you want to update')
    lab.configure(fg = 'black', bg = 'white')
    lab.pack(side = TOP)
    f0.pack(side = TOP)
    f0.config(padx = 5, pady = 5, bg='#FFCCFF')
    f1.pack(side = TOP)
    f1.config(padx = 5, pady = 5, bg = '#FFCCFF')
    f2.pack(side = TOP)
    f2.config(padx = 5, pady = 5, bg = '#FFCCFF')
    f3.pack(side = TOP)
    f3.config(padx = 5, pady = 5, bg = '#FFCCFF')
    r1 = Radiobutton(f1, text = 'Name' , variable = v, value = 1)
    r1.config(fg = 'red',bg = '#FFCCFF')
    r1.pack(side = LEFT)
    r2 = Radiobutton(f1, text = 'Contact' , variable = v, value = 2)
    r2.config(fg = 'red',bg = '#FFCCFF')
    r2.pack(side = LEFT)
    r3 = Radiobutton(f1, text = 'Email Id' , variable = v, value = 3)
    r3.config(fg = 'red' ,bg = '#FFCCFF' )
    r3.pack(side = LEFT)
    r4 = Radiobutton(f1, text = 'Address' , variable = v, value = 4)
    r4.config(fg = 'red',bg = '#FFCCFF')
    r4.pack(side = LEFT)
    la1 = Label(f2 , text = 'Enter the ID of the contact you want to update')
    la2 = Label(f3 , text = 'Enter the New Value of the parameter')
    la1.config(bg = '#FFCCFF')
    la2.config(bg = '#FFCCFF')
    upe1 = Entry(f2)
    upe2 = Entry(f3)
    la1.pack(side = LEFT)
    upe1.pack(side = LEFT)
    la2.pack(side = LEFT)
    upe2.pack(side = LEFT)
    ok_butt_up = Button(f3, text = 'OK' , command = update_exe)
    ok_butt_up.config(relief = 'raised', fg = 'black' , bg = '#E68AB8' , bd =5)
    ok_butt_up.pack(side = RIGHT)    
    

def query_fun():
    query_w = Toplevel()
    query_w.resizable(width = FALSE, height = FALSE)
    query_w.configure(bg = '#FFCCFF')
    query_w.title('QUERYING DATABASE')
    query_w.iconbitmap('icon.ico')
    def query_exe():
        qrs = cnx.cursor()
        sw = Toplevel()
        fq1 = Frame(sw)
        fq2 = Frame(sw)
        if v_main.get() is 1:
            qrs.execute("select _name,id_no from contacts where _name like '%" + se.get()+"%'")
        if v_main.get() is 2:
            qrs.execute("select contact_no,id_no from contacts where contact_no like '%" + se.get()+"%'")
        if v_main.get() is 3:
            qrs.execute("select email_id,id_no from contacts where email_id like '%" + se.get()+"%'")
        if v_main.get() is 4:
            qrs.execute("select date_created,id_no from contacts where date_created like '%" + se.get()+"%'")
        if v_main.get() is 5:
            qrs.execute("select _address,id_no from address where _address like '%" + se.get()+"%'")
        res_q = qrs.fetchall()
        qrs.close()
        def view_exe():
            vrs = cnx.cursor()
            d = 0
            try:
                vrs.execute("drop view apt")
            except mysql.connector.Error as e:
                d = 100
                vrs.execute("create view apt as select c._name,c.contact_no,c.email_id,c.date_created,a._address,a.id_no from contacts c,address a where c.id_no = a.id_no AND c.id_no = '" + id_list[v_sup.get()] + "'")
            if d is 0:
                vrs.execute("create view apt as select c._name,c.contact_no,c.email_id,c.date_created,a._address,a.id_no from contacts c,address a where c.id_no = a.id_no AND c.id_no = '" + id_list[v_sup.get()] + "'")
            
            vrs.execute("select * from apt")
            vw = vrs.fetchall()
            vrs.close()
            #"Name:\t" + str(vw[0]) + "\nContact:\t" + str(vw[1]) + "\nEmail:\t" + str(vw[2]) + "\nDate of creation:\t" + str(vw[3]) + "\nAddress:\t" + str(vw[4]) + "\nId Number:\t" + str(vw[5])
            msg = ''
            g = 0
            for y in vw:
                for x in y:
                    if g is 0:
                        msg = msg + 'Name:\t\t' + str(x)
                    if g is 1:
                        msg = msg + '\n\nContact:\t\t' + str(x)
                    if g is 2:
                        msg = msg + '\n\nEmail:\t\t' + str(x)
                    if g is 3:
                        msg = msg + '\n\nDate of creation:\t\t' + str(x)
                    if g is 4:
                        msg = msg + '\n\nAddress:\t\t' + str(x)
                    if g is 5:
                        msg = msg + '\n\nId Number:\t\t' + str(x)
                    g = g + 1
            tkMessageBox.showinfo(title = "Search Result" , message = msg )
            
        ctr = 0
        v_sup = IntVar()
        id_list = []
        for x in res_q:
            new = Radiobutton(fq1, text = x[0] , selectcolor = 'white', variable= v_sup, value = ctr)
            new.pack(side = TOP)
            id_list.append(x[1])
            ctr = ctr + 1
        se_butt = Button(fq1, text = 'VIEW', command = view_exe)
        se_butt.pack(side = TOP)
        fq1.pack(side = TOP)
        fq2.pack(side = TOP)
        
    def show_all():
        sall = cnx.cursor()
        win_text = Toplevel()
        win_text.resizable(width=FALSE, height=FALSE)
        win_text.title('SHOWING ALL CONTACTS')
        sall_text = Text(win_text, height= 10, width= 150)
        sall_scroll = Scrollbar(win_text)
        sall_scroll.configure(command = sall_text.yview)
        sall_text.configure(yscrollcommand=sall_scroll.set)
        sall_text.pack(side=LEFT)
        sall_scroll.pack(side=RIGHT)
        po = 0
        try:
            sall.execute("drop view drp")
        except mysql.connector.Error as b:
            po=100
            sall.execute("create view drp as select c._name,c.contact_no,c.email_id,c.date_created,a._address,a.id_no from contacts c,address a where c.id_no = a.id_no")
        if po is 0:
            sall.execute("create view drp as select c._name,c.contact_no,c.email_id,c.date_created,a._address,a.id_no from contacts c,address a where c.id_no = a.id_no")
        sall.execute("select * from drp")
        res = sall.fetchall()
        sall.close()
        sall_text.insert(END, 'Name\t\t\tID-Number\t\t\tContact\t\t\tDate_created\t\t\tE-mail\t\t\tAddress\n')
        for x in res:
            for y in x:
                sall_text.insert(END,y)
                sall_text.insert(END,'\t\t\t')
            sall_text.insert(END,'\n') 
    v_main = IntVar()
    fm1 = Frame(query_w)
    fm2 = Frame(query_w)
    fm3 = Frame(query_w)
    la = Label(fm1, text = 'SELECT THE PARAMETER FOR SEARCH')
    la.config(fg = 'black' , bg = '#FFCCFF')
    la.pack(side = TOP)
    rm1 = Radiobutton(fm2, text = 'Name' , selectcolor = 'white', variable = v_main, value = 1)
    rm1.config(fg = 'red')
    rm1.pack(side = LEFT)
    rm2 = Radiobutton(fm2, text = 'Contact' , selectcolor = 'white',variable = v_main, value = 2)
    rm2.config(fg = 'red')
    rm2.pack(side = LEFT)
    rm3 = Radiobutton(fm2, text = 'Email Id' ,selectcolor = 'white', variable = v_main, value = 3)
    rm3.config(fg = 'red')
    rm3.pack(side = LEFT)
    rm4 = Radiobutton(fm2, text = 'Date of Creation' , selectcolor = 'white',variable = v_main, value = 4)
    rm4.config(fg = 'red')
    rm4.pack(side = LEFT)
    rm5 = Radiobutton(fm2, text = 'Address' ,selectcolor = 'white', variable = v_main, value = 5)
    rm5.config(fg = 'red')
    rm5.pack(side = LEFT)
    ls1 = Label(fm3, text = 'Enter the keyword to be searched')
    ls1.config(fg = 'black')
    ls1.pack(side = LEFT)
    se = Entry(fm3)
    se.pack(side = LEFT)
    sb = Button(fm3, text = 'SEARCH' , command = query_exe)
    sb.pack(side = LEFT)
    allb = Button(fm2, text='SHOW ALL', command = show_all)
    allb.pack(side = LEFT)
    fm1.pack(side = TOP)
    fm2.pack(side = TOP)
    fm3.pack(side = TOP)
    
def delete_fun():
    delete_w = Toplevel()
    delete_w.resizable(width = FALSE, height = FALSE)
    delete_w.configure(bg = '#FFCCFF')
    delete_w.title('DELETING CONTACTS')
    delete_w.iconbitmap('icon.ico')
    ser_label = Label(delete_w, text= 'Enter The NAME')
    ser_label.grid(row = 0, column = 0)
    ser_entry = Entry(delete_w)
    ser_entry.grid(row = 0, column = 1)
    def del_exe():
        ser_del = ser_entry.get()
        delete_w.destroy()
        def delete_executed(p):
            crsd = cnx.cursor()
            crsd.execute("delete from contacts where id_no='"+p+"'")
            crsd.execute("delete from address where id_no='"+p+"'")
            crsd.close()
            tkMessageBox.showinfo(title = "DELETION" , message = 'DELETED SUCCESSFULLY' )
            del_w.destroy()
        del_w = Toplevel()
        del_w.title('DELETING CONTACT')
        f1 = Frame(del_w)
        f2 = Frame(del_w)
        del_t = Text(f1, height = 1, width = 150)
        del_e = Entry(f2)
        del_l = Label(f2, text = 'ENTER ID TO BE DELETED')
        del_butt = Button(f2, text = 'OK', command = lambda: delete_executed(del_e.get()))
        scroll = Scrollbar(f1)
        scroll.configure(command = del_t.yview)
        del_t.configure(yscrollcommand = scroll.set)
        f1.pack(side = TOP)
        f2.pack(side = TOP)
        scroll.pack(side = RIGHT, fill = Y)
        del_t.pack(side = LEFT, fill = Y)
        del_l.pack(side = LEFT)
        del_e.pack(side = LEFT)
        del_butt.config(relief = 'raised', fg = 'black' , bg = '#E68AB8' , bd =5)
        del_butt.pack(side =LEFT)
        crsd1 = cnx.cursor()
        crsd1.execute("select c._name,c.id_no,c.contact_no,c.date_created,c.email_id,a._address from contacts c,address a where c._name like '%" + ser_del + "%' AND a._name like '%"+ ser_del+"%' AND c.id_no = a.id_no")
        res = crsd1.fetchall()
        crsd1.close()
        del_t.insert(END, 'Name\t\t\tID-Number\t\t\tContact\t\t\tDate_created\t\t\tE-mail\t\t\tAddress\n')
        for x in res:
            for y in x:
                del_t.insert(END,y)
                del_t.insert(END,'\t\t\t')
            del_t.insert(END,'\n')        
    ok_butt = Button(delete_w, text = 'OK', command = del_exe)
    ok_butt.config(relief = 'raised', fg = 'black' , bg = '#E68AB8' , bd =5)
    ok_butt.grid(row = 1, column = 1)
    
    


db_info  = []

def connect_db():
    try:
        db_info.append(db_name_e.get())
        db_info.append(db_user_e.get())
        db_info.append(db_pass_e.get())
        db_info.append(db_host_e.get())
        global cnx
        cnx = mysql.connector.connect( user = db_info[1], password = db_info[2], host = db_info[3], database = db_info[0] , autocommit = True )
        tkMessageBox.showinfo(title = "RESULT" , message = 'CONNECTED SUCCESSFULLY' )
    except mysql.connector.Error as e:
        root.destroy()
        tkMessageBox.showinfo(title = "RESULT" , message = 'CONNECTION FAILED' )

    
root = Tk()

#defining the entry widget for Database information
db_name_e = Entry(root)
db_user_e = Entry(root)
db_pass_e = Entry(root , show = '*')
db_host_e = Entry(root)

db_name_l = Label(root, text = 'Name of the database')
db_name_l.config(bg = '#C2FFEB')
db_user_l = Label(root, text='Username')
db_user_l.config(bg = '#C2FFEB')
db_pass_l = Label(root, text = 'PassWord')
db_pass_l.config(bg = '#C2FFEB')
db_host_l = Label(root, text = 'Host of the server')
db_host_l.config(bg = '#C2FFEB')

db_label = Label(root, text='Database Login')
db_label.config(height = 1, width = 10 , bg ='#C2FFEB', padx = 2)


#The main label configuartion                     
labelfont1 = ('algerian', 35, 'bold')
root.title('CONTACTS MANAGEMENT WIZARD')
root_label_1 = Label(root, text='CONTACTS MANAGEMENT WIZARD')
root_label_1.config(font = labelfont1, fg='red', bg='#47D1FF', relief = 'solid', bd=YES)
root_label_1.config(height=2 , width = 30)
root_label_1.grid(rowspan = 1, columnspan = 30)
root.resizable(width=FALSE , height=FALSE)

db_label.grid(row = 1 , column = 1)

db_name_l.grid(row = 2, column = 0)
db_user_l.grid(row = 3, column = 0)
db_pass_l.grid(row = 4, column = 0)
db_host_l.grid(row = 5, column = 0)

db_name_e.grid(row = 2, column = 1)
db_user_e.grid(row = 3, column = 1)
db_pass_e.grid(row = 4, column = 1)
db_host_e.grid(row = 5, column = 1)


#Defining all buttons in the root window
button_db_connect = Button(root, text = 'CONNECT' , command = connect_db)
button_db_connect.config( relief = 'raised' , fg = 'black' , bg = '#19FFA3', pady = 1 , bd = 5)
button_db_connect.grid(row = 5, column = 7)

button_add = Button(root, text = 'ADD' , command = add_fun)
button_add.config( relief = 'raised' , fg = 'black' , bg = '#19FFA3' , bd =5)
button_add.grid(row = 11, columnspan = 1)

button_update = Button(root, text = 'UPDATE' , command = update_fun)
button_update.config( relief = 'raised' , fg = 'black' , bg = '#19FFA3', bd =5)
button_update.grid(row = 11, columnspan = 3)

button_query = Button(root, text = 'QUERY', command = query_fun)
button_query.config( relief = 'raised', fg = 'black' , bg = '#19FFA3', bd =5) 
button_query.grid(row = 11, columnspan = 10)

button_delete = Button(root, text = 'DELETE', command = delete_fun)
button_delete.config( relief = 'raised', fg = 'black' , bg = '#19FFA3', bd=5) 
button_delete.grid(row = 11, columnspan = 20)

button_exit = Button(root,text = 'QUIT', command = root.destroy)
button_exit.config( relief = 'raised', fg = 'black' , bg = '#19FFA3' , bd = 5) 
button_exit.grid(row = 14, column = 29)

root.config(bg = '#C2FFEB' , padx = 3, pady = 3)
root.iconbitmap('icon.ico')
root.mainloop()
