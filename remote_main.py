def readtxt(path):
    with open(path,"r") as f:
        result=f.read()
    return result

if __name__ == "__main__": 
    txt=readtxt("./output.txt")