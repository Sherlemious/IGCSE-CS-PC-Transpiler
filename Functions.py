from Errors import *
from Main import *

Line=""
def PRINT(Line):
    Lst1=Line.split()
    printed=""
    
    for w in range(1,len(Lst1)):
        
        word=Lst1[w]
        end=int(len(word))
        if word in vars and word[0]!="\"": #This checks if it is a variable and if the variable exists
            printed+=vars[word]
        else:
            for c in range(end):
                if w==1 and c==0 or w==len(Lst1)-1 and c==end-1:
                    pass
                else:printed+=word[c]
            printed+=" "
        
    print(printed)

    #I Still have to work on all the condition cases in the while. A more effective way should be used in order to 
    #satisfy more compount conditions. The use of dictionaries should be explored

def WHILE(File,Flags,no,vars,Line):
    Lst2=Line.split()
    if Lst2[1] in vars:
        toc1=vars[Lst2[1]]
    elif type(Lst2[1])==float or type(Lst2[1])==int:
        toc1=vars[Lst2[1]]
    op1 = Lst2[2]
    if Lst2[3] in vars:
        toc2=vars[Lst2[3]]
    elif type(Lst2[3])==float or type(Lst2[3])==int:
        toc2=vars[Lst2[3]]
    #Listing comparison scenarios for the Conditions
    if op1=="=":
        Flags[no]=toc1==toc2
    elif op1==">":
        Flags[no]=toc1>toc2
    elif op1=="<":
        Flags[no]=toc1<toc2
    elif op1=="<=":
        Flags[no]=toc1<=toc2
    elif op1==">=":
        Flags[no]=toc1>=toc2
    
    else: print("There is an invalid operand")     
    
    while Line[0:8]!="ENDWHILE" and Flags[no]: #something goes here instead of True (The condition defined in the pseudocode)
        if Line[0:5]=="PRINT":                 #Prints what is supposed to be printed. I still have to work on printing variables after strings
            PRINT(Line)
                
        elif Line[0:5]=="WHILE":
            WHILE(File,Flags,no,vars,Line)


        elif Line[0:6]=="REPEAT":
            pass

        elif Line[0:5]=="INPUT":
            vars[Line[6:len(Line)-1]]=input()

        elif Line[0:3]=="FOR":
            pass

        elif Line[0:2]=="IF":
            IF(Line,vars,Flags)

        #Assignment statement
        else: pass #This part should carry out an assignment statement

    Line=File.readline()


def IF(Line,vars,Flags):
    Lst2=Line.split()
    if Lst2[1] in vars:
        toc1=vars[Lst2[1]]
    elif type(Lst2[1])==float or type(Lst2[1])==int:
        toc1=vars[Lst2[1]]
    op1 = Lst2[2]
    if Lst2[3] in vars:
        toc2=vars[Lst2[3]]
    elif type(Lst2[3])==float or type(Lst2[3])==int:
        toc2=vars[Lst2[3]]
    #Listing comparison scenarios for the 
    if op1=="=":
        Flags.append(toc1==toc2)
    elif op1==">":
        Flags.append(toc1>toc2)
    elif op1=="<":
        Flags.append(toc1<toc2)
    elif op1=="<=":
        Flags.append(toc1<=toc2)
    elif op1==">=":
        Flags.append(toc1>=toc2)
    else: print("There is an invalid operand")

def FOR():
    Lst=Line.split()
    LCV=Lst[1]