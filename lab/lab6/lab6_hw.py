import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

req=requests.get("https://www.scrapethissite.com/pages/simple/")
a=req.content
c=req.text

soup=BeautifulSoup(a,'html.parser')

#unu
countries = soup.find_all('div', class_='col-md-4 country')

for country in countries:
    textname = country.find('h3', class_="country-name").get_text(strip=True)
    print("Country Name:", textname)
    textcapital = country.find('span', class_="country-capital").get_text(strip=True)
    print("Capital:", textcapital)
    textpopulation = country.find('span', class_="country-population").get_text(strip=True)
    print("Population:", textpopulation)
    textarea = country.find('span', class_="country-area").get_text(strip=True)
    print("Area:", textarea)
    print("\n")

#duoăi
data = []

for country in countries:
    textname = country.find('h3', class_="country-name").get_text(strip=True)
    textcapital = country.find('span', class_="country-capital").get_text(strip=True)
    textpopulation = country.find('span', class_="country-population").get_text(strip=True)
    textarea = country.find('span', class_="country-area").get_text(strip=True)
    data.append([textname, textcapital, textpopulation, textarea])

df = pd.DataFrame(data, columns=["CountryName", "Capital", "Population", "Area"])
df.to_excel("countries_info.xlsx", index=False)
print("Excel file 'countries_info.xlsx' created successfully.")
print("\n")

#triei
headers = soup.find_all('li', id=True)
for header in headers:
    print(header.get_text(strip=True)) 
print("\n")  

#pătru
footer = soup.find('div', class_='col-md-12 text-center text-muted').get_text(strip=True)
print(footer)
print("\n")

#șinși
ex6 = soup.find_all('div', class_='col-md-6')  
for ex in ex6:
    print(ex.get_text(strip=True))  
print("\n")