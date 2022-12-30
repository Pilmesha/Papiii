import matplotlib.pyplot
import pandas as pn
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import tkinter as tk
from tkinter import ttk
#კლასი ახალი მონაცემისთვის
class Pollution:
    #კონსტრუქტორი
    def __init__(self, id = "NONE", name = "NONE", gdp = 0.0, organic = 0.0, glass = 0.0, metal=0.0, other=0.0):
        self.__id = id
        self.__name = name
        self.__gdp = gdp
        self.__organic = organic
        self.__glass = glass
        self.__metal = metal
        self.__other = other
    #getter
    def getData(self):
        return (self.__id, self.__name, self.__gdp, self.__organic, self.__glass, self.__metal, self.__other)
#ინტერფეისის კლასი
class GUI:
    def __init__(self,root):
        '''
        :param root: მთავარი ფანჯარა
        ინტერფეისის კონსტრუქტორი
        იქმნება თავდაპირველი ფანჯარა
        '''
        self.root = root
        self.root.config(bg='black')
        root.geometry("500x500")
        self.frame = tk.Frame(master=root)
        self.create_btn = tk.Button(
            master=root,
            text="Create database!",
            width = 25,
            height=5,
            command=self.CreateDB,
            bg='#91ed94',
        )
        self.create_btn.place(x=150,y=0)
        self.n_btn = tk.Button(
            master=root,
            text="Add data",
            fg='#10e078',
            width=20,
            height=3,
            state="disabled",
            command=self.Add_Data,
            bg='black'
        )
        self.n_btn.place(x=330, y=120)
        self.a_btn = tk.Button(
            master=root,
            text="Analise this database",
            fg='#10e078',
            width=20,
            height=3,
            state="disabled",
            command=self.AnaliseData,
            bg='black'
        )
        self.a_btn.place(x=20, y=120)

    def CreateDB(self, event=None):
        '''
        :param event: ამ შემთხვევაში არის დაწკაპუნება
        ვუკავშირდებით სერვერს
        თუ არ არსებობს მონაცამთ ბაზა ვქმნით ახალს
        ვამატებთ ფაილში არსებულ მონაცემებს
        დეაქტივირდება ბაზის შექმნის ღილაკუნა
        აქტივირდება ანალიზის და მონაცემთა დამატების ღიაკუნიები
        '''
        try:
            conn = sqlite3.connect('new_database.db')
        except ConnectionError:
            lbl_error = tk.Label(window, text="Error while connecting")
            lbl_error.place(x=160,y=100)
            window.after(2000, lbl_error.destroy)
        finally:
            lbl = tk.Label(self.root, text="Connected to database...",bg='black',fg='#f0eeed')
            lbl.place(x=170,y=90)
            self.root.after(2000, lbl.destroy)
            lbl1 = tk.Label(self.root, text="Database created...",bg='black',fg='#f0eeed')
            lbl1.place(x=170,y=110)
            self.root.after(2000, lbl1.destroy)
            self.create_btn.config(bg='#313136')
            self.create_btn.config(state='disabled')

            self.a_btn.config(state="active")
            self.n_btn.config(state="active")
            df = pn.read_csv("country_level.csv")
            poll_arr = [x for x in df.values]
            with sqlite3.connect('new_database.db') as conn:
                cursor = conn.cursor()
                conn = """
                    create table if not exists Pollution
                    (
                        Region_ID text,
                        Country_name text,
                        GDP real,
                        Organic_waste real,
                        Glass real,
                        Metal real,
                        Other real
                    )
                    """
                cursor.execute(conn)

                conn = """
                insert or ignore into Pollution (Region_ID, Country_name, GDP, Organic_waste, Glass, Metal, Other)
                values(?,?,?,?,?,?,?)
                """
                cursor.executemany(conn, poll_arr)
            cursor.close()

    def click_ok(self, event = None):
        self.warn_window.after(500, self.warn_window.destroy)

    def Add_Data(self, event=None):
        '''
        :param event: ამ შემთხვევაში არის დაწკაპუნება
        იქმნება ველები მომხმარებლისთვის
        მომხმარებელი ამატებს მონაცემებს
        '''
        lbl_org = tk.Label(master=self.root, text="Organic",bg='black',fg='#f0eeed')
        lbl_org.place(x=440, y=180)
        self.entry_org = tk.Entry(master=self.root, width=10)
        self.entry_org.place(x=375, y=180)

        lbl_glass = tk.Label(master=self.root, text="Glass",bg='black',fg='#f0eeed')
        lbl_glass.place(x=440, y=200)
        self.entry_glass = tk.Entry(master=self.root, width=10)
        self.entry_glass.place(x=375, y=200)

        lbl_metal = tk.Label(master=self.root, text="Metal",bg='black',fg='#f0eeed')
        lbl_metal.place(x=440, y=220)
        self.entry_metal = tk.Entry(master=self.root, width=10)
        self.entry_metal.place(x=375, y=220)

        lbl_other = tk.Label(master=self.root, text="Other",bg='black',fg='#f0eeed')
        lbl_other.place(x=440, y=240)
        self.entry_other = tk.Entry(master=self.root, width=10)
        self.entry_other.place(x=375, y=240)


        lbl_id = tk.Label(master=self.root, text="ID",bg='black',fg='#f0eeed')
        lbl_id.place(x=255, y=180)
        self.entry_id = tk.Entry(master=self.root, width=10)
        self.entry_id.place(x=300, y=180)

        lbl_name = tk.Label(master=self.root, text="Name",bg='black',fg='#f0eeed')
        lbl_name.place(x=255, y=200)
        self.entry_name = tk.Entry(master=self.root, width=10)
        self.entry_name.place(x=300, y=200)

        lbl_gdp = tk.Label(master=self.root, text="GDP",bg='black',fg='#f0eeed')
        lbl_gdp.place(x=255, y=220)
        self.entry_gdp = tk.Entry(master=self.root, width=10)
        self.entry_gdp.place(x=300, y=220)


        create_one_btn = tk.Button(
            master=self.root,
            text="Create data",
            width=10,
            height=2,
            command=self.create_data,
            bg='grey',
            fg='pink'
        )
        create_one_btn.place(x=330,y=270)
    def create_data(self, event=None):
        '''
        იქმნება კალსის ობიექტი რომელსაც აქვს მომხმარებლის მიერ შეტანილი მონაცემები
        მონაცემთა ბაზაში ემატება ობიექტის ველები
        '''
        conn = sqlite3.connect('new_database.db')
        try:
            p = Pollution(
                self.entry_id.get(),
                self.entry_name.get(),
                float(self.entry_gdp.get()),
                float(self.entry_org.get()),
                float(self.entry_glass.get()),
                float(self.entry_metal.get()),
                float(self.entry_other.get())
            )
            with sqlite3.connect('new_database.db') as conn:
                cursor = conn.cursor()
                self.conn = """
                        insert or ignore into Pollution (Region_ID, Country_name, GDP, Organic_waste, Glass, Metal, Other)
                        values 
                        (?,?,?,?,?,?,?)
                    """
                tup = p.getData()
                cursor.execute(self.conn, tup)
            # ველების გასუფთავაება
            self.entry_id.delete(0, 'end')
            self.entry_name.delete(0, 'end')
            self.entry_gdp.delete(0, 'end')
            self.entry_org.delete(0, 'end')
            self.entry_glass.delete(0, 'end')
            self.entry_metal.delete(0, 'end')
            self.entry_other.delete(0, 'end')

        #თავს ვარიდებთ შეცდომას, როდესაც მომხმარებელს ველში არასწორი ტიპის მონაცემი შეყავს
        except ValueError:
            #შეცდომის ფანჯრის შეცმნა
            self.warn_window = tk.Tk(className="Warning!")
            self.warn_window.geometry("300x300")
            lbl_error = tk.Label(master=self.warn_window, text="Invalid type!")
            lbl_error.pack()
            ok_btn = tk.Button(
                master=self.warn_window,
                text="OK",
                command=self.click_ok,
                width=20,
                height=5
            )
            ok_btn.pack()

    def AnaliseData(self, event=None):
        #მომხმარებლისთვის ჩამოსაშლელი მენიუები და ველები იქმნება

        #დიაგრამის ტიპი
        lbl_diagtype = tk.Label(master=self.root, text="Diagram type",bg='black',fg='#f0eeed')
        lbl_diagtype.place(x=20,y=180)
        box_diagtype = ttk.Combobox(master=self.root, width=12, state='readonly')
        box_diagtype['values'] = ["Scatter", "Bar", "Barh", "Pie", "Line"]
        box_diagtype.place(x=100, y=180)

        #x კოორდინატის არჩევა
        lbl_xcoord = tk.Label(master=self.root, text="X Coordinate",bg='black',fg='#f0eeed')
        lbl_xcoord.place(x=20,y=210)
        box_xcoord = ttk.Combobox(master=self.root, width=12, state='readonly')
        self.con = sqlite3.connect('new_database.db')
        self.df = pn.read_sql_query("select * from Pollution", self.con)
        val  = [x for x in self.df.keys().values]
        box_xcoord['values'] = val
        box_xcoord.place(x=100, y=210)

        #Y კოორდინატის არჩევა
        lbl_ycoord = tk.Label(master=self.root, text="Y Coordinate",bg='black',fg='#f0eeed')
        lbl_ycoord.place(x=20, y=240)
        box_ycoord = ttk.Combobox(master=self.root, width=12, state='readonly')
        box_ycoord['values'] = val
        box_ycoord.place(x=100, y=240)

        #დიარგამის ფერის არჩევა
        lbl_color = tk.Label(master=self.root, text="Color",bg='black',fg='#f0eeed')
        lbl_color.place(x=20, y=270)
        box_color = ttk.Combobox(master=self.root, width=12, state='readonly')
        colors = [
                "blue",
                "green",
                "red",
                "cyan",
                "magenta",
                "yellow",
                "black",
                "white"
            ]
        box_color['values'] = colors
        box_color.place(x=100,y=270)
        btn_analise = tk.Button(
            master=self.root,
            text="Analise",
            width=10,
            height=2,
            command=lambda : self.DrawGraphs(None, box_xcoord.get(), box_ycoord.get(), box_diagtype.get().lower(), box_color.get()),
            bg='grey',
            fg='pink')
        btn_analise.place(x=100, y=300)

    def DrawGraphs(self, event ,ind, val, type, color):
        '''
        :param event: დაწკაპურნება
        :param ind: იქს კოორდინატი
        :param val: იგრეკ კოორდინატი
        :param type: დიაგრამის ტიპი
        :param color: დიაგრამის ფერი
        :return: გამოსახავს დიაგამას იმისდა მიხედვით, თუ რა დიაგრამის ტიპი, ფერი და დაჯგუფების მონაცემები გადასცა მომხმარებელმა
        '''
        try:
            df1 = self.df[val].groupby(self.df[ind]) #დაჯგუფება არგუმენტების მიხედვით
            index = np.array(df1.count().index, dtype="str")
            value = np.array(df1.sum())
            dat = pn.DataFrame({
                ind: index,
                val: value,
            })
            if type == 'pie':
                dat = plt.pie(value, labels=index, shadow = True, autopct='%1.1f%%')
            else:
                dat.plot(kind=type, x=ind, y=val, color=color)
            plt.show() #დიაგრამის გამოსახვა
        #თავს ვარიდებთ შეცდომას, როდესაც მომხმარებელი სავალდებულო ველებს არ ავსებს
        except KeyError:
            #შეცდომის ფანჯრის გამოტანა
            self.warn_window = tk.Tk(className="Warning!")
            self.warn_window.geometry("300x300")
            lbl_error = tk.Label(master=self.warn_window, text="One of the fields is empty")
            lbl_error.pack()
            ok_btn = tk.Button(
                master=self.warn_window,
                text="OK",
                command=self.click_ok,
                width=20,
                height=5
            )
            ok_btn.pack()

if __name__ == '__main__':
    window = tk.Tk(className="Your whore")
    App = GUI(window)
    window.mainloop()