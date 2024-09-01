import requests
from bs4 import BeautifulSoup as bs
from customtkinter import *

oyna=CTk()
oyna.title('m._.nazarbek')
oyna.geometry('500x600')



def find_rating():
    nickname=nickname_entry.get()
    try:
        url=requests.get(f'https://lichess.org/@/{nickname}/perf/{combo.get()}')
        s=bs(url.content,'html.parser')
        s1=s.find('div',class_='is2d')
        s2=s1.find('div',class_=f'page-menu__content box perf-stat {combo.get()}')
        s3=s2.find('div',class_='box__pad perf-stat__content')
        s4=s3.find('section',class_='glicko')
        rapid_rating=str(s4.find('h2').find('strong'))[8:-9]
        if rapid_rating=='?':
            result_label.configure(text=f'{nickname} hali {combo.get()} rejimida o\'yin o\'ynamagan')
        else:
            result_label.configure(text=f'Hozirgi vaqtda {nickname}ning {combo.get()} reytingi: {rapid_rating}')
    except AttributeError:
        result_label.configure(text='Bunday foydalanuvchi topilmadi!')

        
combo=CTkComboBox(oyna,values=['rapid','classical','blitz','bullet'],font=('Arial',30),width=170)
combo.place(relx=0.5,rely=0.15,anchor='center')



nickname_entry=CTkEntry(oyna,placeholder_text='Nickname...',font=('Arial',20),width=200)
nickname_entry.place(relx=0.5,rely=0.35,anchor='center')

find_button=CTkButton(oyna,text='Find',font=('Arial',30),corner_radius=16,command=find_rating)
find_button.place(relx=0.5,rely=0.5,anchor='center')

result_label=CTkLabel(oyna,text='',font=('Arial',20))
result_label.place(relx=0.5,rely=0.75,anchor='center')

oyna.mainloop()
