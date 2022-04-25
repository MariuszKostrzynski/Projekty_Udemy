from tkinter import *
from tkcalendar import *
import tkinter as tk
import datetime
import requests
import csv

# Ceate window object
app = tk.Tk()
app.title('ADAO - Aplikacja Do Analizy Opadów')
app.geometry('800x500')

variable = tk.StringVar()
label = tk.Label(app, justify=CENTER, anchor="center", textvariable=variable, font=('Tahoma', 11), padx=20, pady=20)
variable.set("Witamy w aplikacji do analizy opadów.\n""\n"
              "Chcąc uzyskać dane do analizy proszę wybierz:\n "
              "1) Dzień z którego chcesz otrzymać dane\n "
              "2) Lokalizację stacji pogodowej (Legenda)\n "
              "3) Rodzaj pomiaru (Legenda)\n")

label.grid(row=1, column=1, padx=10, pady=10)

frame = LabelFrame(app, text="Calendar", padx=15, pady=15)
frame.grid(row=2, column=1, padx=10, pady=10)

today = datetime.date.today()

cal = DateEntry(frame, selectmode="day")
cal.grid(row=2, column=3, padx=10, pady=10)

def grab_date():
    my_date_label.config(text=cal.get_date())
    date1 = cal.get_date()
    date = date1.strftime("%Y-%d-%m")
    return date

my_button = Button(app, width=20, height=2, text="Wybierz datę", activebackground="grey", cursor="tcross", command=grab_date)
my_button.grid(row=2, column=2, padx=10, pady=10)

my_date_label = Label(app, font=('bold', 12))
my_date_label.grid(row=2, column=4, padx=50, pady=10)

# access_token = "f3fd424983f545baa965034aa976393b"
#
# station_id = "1"
# data_type = "rain"

# def get_data(station_id, data_type, date):
#     url = f"https://pomiary.gdanskiewody.pl/rest/measurements/{station_id}/{data_type}/{date}"
#     headers = {
#         'Authorization': 'Bearer {}'.format(access_token)
#     }
#     response = requests.get(url, headers=headers)
#     wheater_date_json = response.json()
#     wheater_date_string = wheater_date_json['data']
#     return wheater_date_string
#
#
# write_file = 'C:/Users/Mariola/WSB_python_pandas/homework/nauka/praca_Motlawa/PRACA_PODYPLOMOWA/opady.csv'  #podaję ścieżkę gdzie ma zapisać plik csv
# with open(write_file, 'w', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     data = get_data(station_id, data_type, grab_date())
#     for datapoint in data:
#         writer.writerow(datapoint) #wyciągam dane z datą ze słownika dict

def show_legend():
    newWindow = Toplevel(app)
    # sets the title of the
    # Toplevel widget
    newWindow.title("Legenda")
    # sets the geometry of toplevel
    newWindow.geometry("600x400")
    label = Text(newWindow)
    label.insert(INSERT, "\n".join(options))
    label.pack()
    # dropdown_list = Label(openNewWindow(), text=clicked.get()).pack()

options = [
    '',
    'https://pomiary.gdanskiewody.pl/rest/measurements/numer_stacji/symbol_pomiaru/data',
    'gdzie:',
    'numer_stacji - numer stacji zgodny z numerem zwracanym w liście stacji',
    '',
    'Symbol_pomiaru - jedna z wartości:',
    'rain - opad',
    'water - poziom wody',
    'winddir - kierunek wiatru',
    'windlevel - siła wiatru',
    'temp - temperatura',
    'pressure - ciśnienie atm.',
    'humidity - wilgotność',
    'sun - nasłonecznienie',
    '',
    'Data pomiaru',
    'data - data pomiaru w formacie rrrr-mm-dd',
]


def selected(event):
    myLabel = Label(app, text=clicked.get()).grid(row=4, column=1, padx = 10, pady=10)


options1 = [
    '1 - Dolne Miasto',
    '2 - Górki Zachodnie',
    '4 - Kubacza',
    '6 - Zb.Wileńska',
    '7 - Reja',
    '8 - Matemblewo',
    '9 - Oliwa/IBWPAN',
    '10 - Osowa',
    '11 - Kiełpino Górne',
    '12 - Jasień',
    '13 - Matemblewoprzepust',
    '15 - Ogrodowa',
    '16 - Matarnia',
    '17 - RówS-1zbiornikJabłoniowa',
    '18 - Cygańska Góra',
    '19 - Jez.Jasień',
    '20 - ZbiornikOgrodowa',
    '21 - ZbiornikJasień',
    '22 - ZbiornikNowiec2',
    '23 - Zbiornik Srebrniki',
    '24 - ZbiornikGórneMłyny',
    '25 - ZbiornikKiełpinek',
    '26 - pow.zb.Srebrniki',
    '27 - Zbiornik Uphagena',
    '28 - Ujście',
    '31 - Szadółki/ZUT',
    '35 - Nowy Port',
    '40 - Matarnicki Pot.',
    '91 - Sopotopad-ul.Świemirowska',
    '92 - Sopotopadul.Polna',
    '93 - Sopotopadul.Haffnera',
    '94 - Sopotopadul.Kolberga',
    '95 - SopotZbiornikOkrzei-wzlewniKarlikowskiegoPotoku',
    '96 - SopotZbiornikKochanowski-wzlewniKarlikowskiegoPotoku',
    '97 - SopotZbiornikObodrzyców-KamiennyPotok',
    '201 - Zb.OrłowskaII',
    '202 - RówMM1KDZbiornik Barniewice',
    '203 - Zb.Owczarnia',
    '204 - RówMZbiornik Klukowo',
    '205 - RówMM4KDZbiornik Rębiechowo',
    '206 - Zb.14-Bytowska4A',
    '207 - Zb.12-Bytowska4',
    '208 - Zb.11-Kuźnia',
    '209 - Zb.8-Spacerowa',
    '210 - Zb.6-Opacka',
    '211 - Zb5-Grunwaldzka',
    '212 - Zb.4-Subisława',
    '213 - Zb.3-Chłopska',
    '214 - Zb2-Orłowska',
    '215 - Zb.1Jelitkowska',
    '216 - Zbiornik Budowlanych',
    '218 - RówS-1dopływPzbiornikCedrowa',
    '219 - RówS-1zbiornikŁabędzia',
    '220 - ZbiornikMyśliwska',
    '221 - ZbiornikZabornia',
    '222 - DopływLZbiornikMokraFosa',
    '223 - KDZbiornikMadalińskiego',
    '224 - KDZbiornikPlatynowa',
    '225 - ZbiornikŚwiętokrzyskaI-Rębowo',
    '226 - ZbiornikŚwiętokrzyskaII-Łostowice',
    '228 - dopływL-zbiornikWieżycka',
    '229 - KDzb.Warszawska',
    '230 - KDzb.Przemyska-Białostocka',
    '231 - KDzb.Jeleniogórska',
    '232 - ZbiornikAugustowska',
    '233 - MaćkowyPot.ZbiornikKolorowy',
    '234 - Św.Wojciech',
    '235 - Lipce-poniżejMaćkowyPot.',
    '236 - Orunia-poniżejOruńskiPot.',
    '237 - Nakielska-poniżejKDMałomiejska',
    '238 - Cienista',
    '239 - Zaroślak',
    '240 - IBWPAN',
    '241 - Katedra',
    '242 - Wrzeszcz Słowackiego36A',
    '243 - Wrzeszcz Aldony',
    '244 - Bieszczadzka',
    '245 - ParkOrunski',
    '246 - WlotzbiornikŚwiętokrzyskaI',
    '247 - Św.WojciechPot.poniżejBorkowskiPot.',
    '248 - KowalskiPot',
    '250 - UMGdańsk',
    '251 - JanaPawłaIIH',
    '252 - Jaśkowa Dol./Sobótki',
    '253 - RynarzewskiPot.',
    '254 - PortPn',
    '255 - M.WisłaStogi',
    '256 - UM3majakom.KDPn',
    '257 - UM3Majakom.KDPd',
    '301 - Klukowo',
    '302 - Jelitkowo',
    '303 - Brzeźno',
    '305 - Zabornia',
    '306 - Łostowice',
    '307 - Śródmieście/GóraGradowa',
    '308 - PotokBorkowski/Starogardzka',
    '309 - Przegalina',
    '310 - Stogi/Kaczeńce',
    '311 - Chełm/Dragana',
    '312 - Oliwa/PotokKołobrzeski',
    '313 - Lipce/TraktŚw.Wojciecha',
    '501 - GdyniaChylonia/Pogorze',
    '502 - GdyniaOrłowo',
    '503 - GdyniaChwarzno',
    '505 - GdyniaOksywie',
    '510 - GdyniaBulwar',
    '512 - GdyniaDąbrowa',
    '525 - GdyniaQkol.Lotników',
    '551 - GdyniaKaczeBukiP',
    '552 - WejherowoP',
    '553 - GdyniaOrłowoP',
    '554 - RumiaJanowoP',
    '555 - Gdynia PortP',
    '999 - Sobieskiego',
]

clicked = StringVar()
clicked.set(options1[0])

drop = OptionMenu(app, clicked, *options1, command=selected)
drop.grid(row=3, column=1, pady=20)
# a button widget which will open a
# new window on button click
btn = Button(app, text="LEGENDA", command=show_legend)
btn.grid(row=1, column=2)

tk.mainloop()
# app.mainloop()
