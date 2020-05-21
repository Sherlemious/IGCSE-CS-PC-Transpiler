from Functions import *
vars={}
Flags={}
no=0
File = open("F:\\Programming\\Python\\Projects\\IGCSE-CS-PC-Compiler\\To be translated","r")
for Line in File:                          #Iterates through the lines until no more lines are available
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
    
    no+=1