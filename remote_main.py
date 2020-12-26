import pandas as pd
import matplotlib.pyplot as plt

def readtxt(path):
    with open(path,"r") as f:
        result=f.read()
    return result

def txt_to_list(txt):
    plaintext=txt.split("<my_cutting_tag>")[:-1]
    resultLIST=[]
    for i in plaintext:
        resultLIST.append(eval(i))
    return resultLIST

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

if __name__ == "__main__": 
    txt=readtxt("./output.txt")
    playerLIST=txt_to_list(txt)
    playerDF=pd.DataFrame(playerLIST)
    print(playerDF)
    makePlot(playerDF)