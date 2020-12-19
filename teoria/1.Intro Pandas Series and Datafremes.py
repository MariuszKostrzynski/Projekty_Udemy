# dokumentacja https://pandas.pydata.org/docs/
#data analist, bi analist
import pandas as pd

#dataframe tablica dwuwymiarowa o rzędach i kolumnach

df = pd.DataFrame(
    {
        'kolumna_imie' : ['Piotr', 'Adam', 'Maria', 'Michał'],
        'kolumna_nazwisko' : ['Kowalski', 'Słowik', 'Kowalska', 'Micha']
    }
)
#
# print(df)
#########################################################################################
df2 = pd.DataFrame(
    data= [
        ['Piotr', 'Kowalski'],
        ['Adam', 'Slowik'],
        ['Maria', 'Kowalska'],
        ['Michał', 'Slowik']
    ], columns= ['name', 'surname'], index=['1', '2', '3', '4'])
# print(df2)
# print(df2.head(3))
# print(type(df2))

#####################################################################################
# pokazuje ilość kolumn i wierszy
# print(df.shape)
# # długość tabeli ilość id
# print(len(df))

#####################################################################################
#konwersja tabeli na słownik
# df_dict = df.to_dict()
# print(df_dict)

######################################################################################
#konwersja ze słownika do dataframe

my_dict = {
    'kolumna_imie': {0: 'Piotr', 1: 'Adam', 2: 'Maria', 3: 'Michał'},
    'kolumna_nazwisko': {0: 'Kowalski', 1: 'Słowik', 2: 'Kowalska', 3: 'Micha'}
}

from_dict_df = pd.DataFrame.from_dict(my_dict)
# print('from dict')
# print(from_dict_df)

#######################################################################################
#print("ten dataframe posiada {} kolumn oraz {} wierszy". format( df.shape[0], df.shape[1]))


#########################################################################################
#sprawdzanie typów danych
# print(df.dtypes)

#########################################################################################
#szczegółowa informacja odnośnie całego DataFrame
#df.info()

#########################################################################################
#przypisywanie wartości do kolumn
df["kolumna_imie"] = "Adam"
# print(df)

#########################################################################################
#dodawanie nowej kolumny z definiowaną nazwę

df['New_column'] = 'Maria'
# print(df)

#########################################################################################
#kopiowanie kolumn
df['copy_nazwisko'] = df['kolumna_nazwisko']

#kopiowanie dataframe
# new_df = pd.DataFrame(
#     {
#         'a': [10, 20, 30],
#         'b': [20, 30, 40]
#     }
# )

# print('new_df')
# print(new_df)
#
# copy_df = new_df.copy()
# print('copy_df')
# print(copy_df)

# new_df['a'] = new_df['b'] + 1
# print(copy_df)
# print(new_df)

#wyznaczanie podanych kolumn, poprzez nawias kwadratowy
# new_df = new_df[['b', 'a']]
# print(new_df)

#####################################
# **pandas Series()
dane= ['Piotr', 'Adam', 'Maria', 'Michal']

sr = pd.Series(
    data = dane, name='imiona'
)
# print(sr)
#
# print(type(sr))
#
# print(len(sr))

# print(
#     sr.str.len()
# )

###############################
#stworzenie kolumny zawierającej liczbę liter z kolumny 'Kolumna_nazwisko
df['len_nazwiska'] = df['kolumna_nazwisko'].str.len()
#print(df)

####################################################################################
#konwersja pd.Series do listy
surname_list = df['kolumna_nazwisko'].tolist()
#print(surname_list)
###################################################################################

df['new_names'] = sr
print(df)

##################################################################################
#konwersja do pd.Series do DateFrame()
#met 1
# df_from_sr=sr.to_frame()
# print(type(df_from_sr))
# print(df_from_sr)

#met 2
# df_from_sr = pd.DataFrame(sr)
# print(df_from_sr)






