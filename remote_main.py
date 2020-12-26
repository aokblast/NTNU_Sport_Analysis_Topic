def readtxt(path):
    with open(path,"r") as f:
        result=f.read()
    return result

def txt_to_array(txt):
    plaintext=txt.split("<my_cutting_tag>")[:-1]
    resultLIST=[]
    for i in plaintext:
        resultLIST.append(eval(i))
    return resultLIST

if __name__ == "__main__": 
    txt=readtxt("./output.txt")
    txt=txt_to_array(txt)
    