from lxml import html
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import zipfile

##### FETCHING THE URL AND REQUEST RESPONSE ########

url = 'https://www.sec.gov/foia/iareports/inva-archive.htm'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

###### FOR PANDAS DATAFRAME #######
d = []
cols = ['Date', 'Link', 'Type']

###### SCRAPPING WEBSITE HAVING 'a' TAG AND STARTING WITH RE /foia #######

for link in soup.find_all("a",href = re.compile('/foia')):

    links = link.get('href')

    # CREATING 'TYPE' COLUMNS HAVING EXEMPT, NON-EXEMPT
    if re.search("exempt" , links):
        type = "Exempt"
    else:
        type = "Non-Exempt"

    # RETRIEVING DATES FROM THE LINK
    if re.search("\d+",links):
        dates =  int(''.join([x for x in links if x.isdigit()]))

        #FORMATING DATE IN THE FORM YY-MM-DD
        x = str(dates)
        if len(x) > 5 :
            mm = x[0:2]
            dd = x[2:4]
            yy = x[4:6]
            timestamp = yy + '-'+ mm +'-' + dd
        else:
            mm = x[0:1]
            dd = x[1:3]
            yy = x[3:5]
            timestamp =  yy + '-'+ mm +'-' + dd


    d.append([timestamp,links,type ])
    df = pd.DataFrame(d, columns=cols)
    df2 = df.set_index('Date')
    df1 = df.set_index('Date')

#######  Function 1 ##########
# After scraping data from website storing it in Pandas dataframe
def sec_dataframe():
    df = pd.DataFrame(d, columns=cols)
    print(df1)


##### Function 2 ######
# YOU CAN CALL FUNCTION USING PERIODS(First way to call the function)

def get_sec_zip_by_period(str, str1 , str2):

    list = [str , str1 , str2]
    df3 = df2.ix[list]
    print(df3)

###### CALLING THE Function 1 & 2 #####
sec_dataframe()
get_sec_zip_by_period("17-4-03" , "07-5-07" , "12-12-05")
