import re
def strcheck(x):
    return re.findall(r"Test([\d.]*\d+)", x)

arraybas = input("Please type how many number you will use (between 0 and 100):")

strcheck(arraybas)

arraynumber = int(arraybas)


posnum = []
negnum = []
zernum = []
def plusMinus(x):
    if x<0:
       return negnum.append(x)
    elif x>0:
       return posnum.append(x)
    else:
       return  zernum.append(x)


f = range(arraynumber)
for x in f:
    usernumber = input("Number (between -100 and 100):")
    i=0
    while i < 100:
        i += 1
        if int(usernumber)<-100 or int(usernumber)>100:
            usernumber = input("Opps! Number Again (between -100 and 100):")

        else:
            break


    plusMinus(int(usernumber))

print(posnum, negnum, zernum)

rspos = "{:.6f}".format((len(posnum))/arraynumber)
rsneg = "{:.6f}".format((len(negnum))/arraynumber)
rszer = "{:.6f}".format((len(zernum))/arraynumber)

print(rspos,rsneg,rszer)
