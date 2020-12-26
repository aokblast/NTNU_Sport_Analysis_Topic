import requests as rq
from bs4 import BeautifulSoup as bs4
import pandas as pd
import matplotlib.pyplot as plt
import csv

idDF=pd.read_excel(r'./SFBB-Player-ID-Map.xlsx',engine='openpyxl')

def writetxt(playerLIST):
    with open('output.txt',"w",newline='\n') as f:
        for i in playerLIST:
            f.writeline(i)
            
def getContent(url):
    response=rq.get(url)
    soup=bs4(response.text,"lxml")
    return soup

def getSalary(num):
    url="https://www.usatoday.com/sports/mlb/salaries/"
    content=getContent(url)
    table=content.find_all("tr")[1:num+1]
    resultLIST=[]
    for i in table:
        name=i.find(class_="sp-details-open").text.strip()
        salary=int(i.find(class_="salary").text.strip().replace("$","").replace(",",""))
        resultLIST.append({"Name":name,"Salary":salary})
    return resultLIST

def getPlayerID(name):
    return int((idDF.loc[idDF['PLAYERNAME']==name])['MLBID'])

def getPlayerData(LIST,num):
    fig=plt.figure()
    for i in range(num):
        name=LIST[i]['Name']
        id=str(getPlayerID(name))
        name=name.replace(" ","-").lower()
        url="https://www.mlb.com/player/"+name+"-"+id
        content=getContent(url)
        table=content.find("div",class_="career")
        thead=table.find("thead").find_all("span")[1:]
        data=table.find("tr",attrs={"data-index":"0"}).find_all("span")[1:]
        for j in range(len(thead)):
            title=thead[j].text.split("-")
            ans=data[j].text.split("-")
            for h in range(len(title)):
                LIST[i][title[h]]=float(ans[h])

def makePlot(DF):
    cnt=0
    col=DF.columns[1:]
    labels=DF["Name"].values.tolist()
    fig, axes = plt.subplots(nrows=(len(col)//4 if len(col)%4==0 else len(col)//4+1), ncols=4)
    for i in col:
        DF.pivot(values=i,columns='Name').plot(kind='bar',ax=axes[cnt//4,cnt%4],title=i,linewidth=5.0).legend_.remove()
        cnt+=1
    fig.legend(labels)
    plt.show()

if __name__=="__main__":
    num=int(input("Please enter the number you want to show:"))
    playerLIST=getSalary(num)
    getPlayerData(playerLIST,num)
    writetxt(playerLIST)
    playerDF=pd.DataFrame(playerLIST)
    print(playerDF)
    makePlot(playerDF)
