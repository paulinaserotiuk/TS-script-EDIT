import pandas as pd
import csv


#tworze zmienne prowadzace do plikow z danymi z Clarity (Dane z lista pracownikow) i Personio (dane z TS)

#tu podmiana plikow za kazdym razem
File_Clarity2 = '/Users/paulinaserotiuk/Desktop/Clarity2.xlsx'
File_Personio = '/Users/paulinaserotiuk/Desktop/PersonioDane.xlsx'

#wykorzystuje metode read z pd zeby czytac pliki

#dla pliku Clarity
read_Clarity2_excel = pd.read_excel(File_Clarity2, 'Sheet1', index_col=None)

#tu podmiana plikow za kazdym razem
read_Clarity2_excel.to_csv('/Users/paulinaserotiuk/Desktop/Clarity2.csv', encoding='utf-8')

#dla pliku Personio
read_Personio_excel = pd.read_excel(File_Personio, 'ZB_EXPORT_LA_DIT', index_col=None)

#tu podmiana plikow za kazdym razem
read_Personio_excel.to_csv('/Users/paulinaserotiuk/Desktop/Personio.csv', encoding='utf-8')

#filtruje plik csv zeby otrzymac liste pracownikow o statusie Active ORAZ nalezacych do dzialow Tech i S&D
#czytam plik
Clarity2_data = pd.read_csv('/Users/paulinaserotiuk/Desktop/Clarity2.csv')
Personio_data = pd.read_csv('/Users/paulinaserotiuk/Desktop/Personio.csv')

Clarity2_data = Clarity2_data.rename(columns={'Company ': 'Company'})

#filtr na Active
Clarity2_data_active = (Clarity2_data[Clarity2_data.Status=="Active"])
#print(Clarity2_data_active)

#print(Clarity2_data_active.columns.values)

Clarity2_data_active_notTCS=(Clarity2_data_active[Clarity2_data_active.Company != "TATA TCS (57050818)"])
#print(Clarity2_data_active_notTCS)

#filtr na Tech
Clarity2_data_active_tech = (Clarity2_data_active_notTCS[Clarity2_data_active_notTCS.Department=="Technology"])

#Filtr na S&D
Clarity2_data_active_sd = (Clarity2_data_active_notTCS[Clarity2_data_active_notTCS.Department=="Strategy&Delivery"])


#dodajemy so siebie odbydwie data frames

sum_of_tech_sd = pd.concat([Clarity2_data_active_sd, Clarity2_data_active_tech])

#parsuej data frame do listy zeby porownac z lista z personio
sum_of_tech_sd_list = sum_of_tech_sd["Employee number"].tolist()


#Wyciagam enumery z pliku Personio i dodaje do listy
Personio_enumer_array = []
Personio_input_file = csv.DictReader(open("/Users/paulinaserotiuk/Desktop/Personio.csv"))
for row in Personio_input_file:
    Personio_enumer_array.append(row['MITARBEITER_ID'])

#print(Personio_enumer_array)
#print(len(Personio_enumer_array))

#Wyciagam enumery z pliku Clarity i dodaje do listy
Clarity2_enumer_array = []
Clarity2_input_file = csv.DictReader(open("/Users/paulinaserotiuk/Desktop/Clarity2.csv"))
for row in Clarity2_input_file:
   Clarity2_enumer_array.append(row['Employee number'])

#print(Clarity2_enumer_array)
#print(len(Clarity2_enumer_array))

#porownuje enumery z obydwu list i dodaje do listy te ktotych nie ma w pliku personio (czyli nie zaraportowaly czasu)
missing_enumer_array = []
for enumer in Clarity2_enumer_array:
    if enumer in Personio_enumer_array:
       pass
    else:
       missing_enumer_array.append(enumer)

#print(type(missing_enumer_array))
#print(missing_enumer_array)

#porownuje liste active z tech i sd z lista employees ktorych enumer nie pojawia sie w TS
missing_enumer_array_final = []
for item in missing_enumer_array:
    if item in sum_of_tech_sd_list:
        missing_enumer_array_final.append(item)
#print(missing_enumer_array_final)
#print(type(missing_enumer_array_final))


#wyciagam  employees numbers i emaile
email_number_list = []
number_list = []
Clarity2_csv = '/Users/paulinaserotiuk/Desktop/Clarity2.csv'
with open(Clarity2_csv) as fh:
    reader = csv.DictReader(fh, delimiter=',')
    for row in reader:
      email_number_tup = list((row['Employee number'], row['Email']))
      email_number_list.append(email_number_tup)

#print(email_number_list)

#porownanie missing enumbers z pliku TS ze wsyztskimi enumerami i  wyciagniecia emaili
final_list = []

for enumer, email in email_number_list:
    if enumer in missing_enumer_array_final:
        final_list.append(email)

print(final_list)
print(len(final_list))

df_emails = pd.DataFrame(data={"col1": final_list})
#tu stworzenie nowego pliku za kazdym razem
df_emails.to_csv("/Users/paulinaserotiuk/Desktop/Emails.csv", sep=',',index=False)

#IMPORTANT - how to extract email adresses (redo the dicitonary?) or the vlookup DONE!
#write the emails to a file DONE
#Set up email sending - DONE, just have to resolve the 2step authent issue - need to set up a special account
#we have to discuss the form of the files - has to be the same every week
#are the filtering criteria ok? ADD TCS TATA filetring out
#agree on the process - who sends the files, when? consistency of the forms




