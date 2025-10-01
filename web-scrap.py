import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_Name=[]
Prices=[]
Description=[]
Reviews=[]


for i in range (2,12):

    url='https://www.flipkart.com/search?q=mobile+phone+under+15000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_12_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_12_na_na_na&as-pos=3&as-type=RECENT&suggestionId=mobile+phone+under+15000&requestId=b56fa4bd-fca4-4903-922b-12590a8d4fff&as-searchtext=mobile%20phone%20under%2015000='+ str(i)

    r = requests.get(url)
    #print(r)

    soup = BeautifulSoup(r.text, "lxml")

    box= soup.find("div", class_="DOjaWF gdgoEp")
        

    names=box.find_all('div',class_='KzDlHZ')
    #print(names)

    for i in names:
     name = i.text
     Product_Name.append(name)

    #print(Product_Name)

    Price=box.find_all('div',class_='Nx9bqj _4b5DiR')

    for i in Price:
     name= i.text
     Prices.append(name)
    #print(Prices)

    desc=box.find_all('ul',class_="G4BRas")

    for i in desc:

        name=i.text
        Description.append(name)
    #print(Description)


    Rev=box.find_all("div",class_="XQDdHH")

    for i in Rev:
     name=i.text
     Reviews.append(name)

    #print(Reviews)


df = pd.DataFrame({"Product Name":Product_Name, "Price":Prices, "desc":Description,"Reviwe":Reviews})

#print(df)
df.to_csv("flipkart_mobile_Data.csv")