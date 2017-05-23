

import csv
import re
import string

if __name__ == "__main__":


    keggfile = "C:\Users\dekai\Desktop\USF Database\kegg_raw.txt"
    kegg = open(keggfile,'r')
    actions = ["inhibitor","substrate","inducer"]
    begin = ["B ","C ", "D "]
    vitros = ["Weak", "Moderate", "Strong", "Narrow", "Sensitive"]
    db = open("C:\Users\dekai\Desktop\USF Database\kegg.csv",'wb')
    fkegg = csv.writer(db,delimiter=",")
    fulldb=[]
    
    rem = "CYP"

    header=["Drug", "CYP***", "Action","Species", "Database","refence_1", "reference_2","reference_3","Strength"]
    fkegg.writerow(header)
    
    for line in kegg:
        strength=[]
        drug = []
        
        accessed=[]
        count = 0
        for i in actions:
            if i in line:
                action = i

        if begin[0] in line:
            temp = line.split()
            temp = temp[1]
            temp = re.sub(rem,'',temp)
            cypid = temp

        if begin[1] in line:
            temp = line.split()
            for i in vitros:
                if i in temp:
                    strength.append(i)

            power = ' & '.join(strength)
            #power = power.replace(',','')
            

        if begin[2] in line:
            temp = line.split()
           
            for i in temp:
                if count > 1:
                    drug.append(i)
                    
                count=count+1
            dname=' '.join(drug)
            dname = dname.replace(',','')
        if len(drug) > 0:
            accessed= [dname,cypid,action,"Not Specified","KEGG",'','','',power]
            fulldb.append(accessed)


   
    for i in fulldb:
        temp = str(i)
        temp = temp.replace('[','')
        temp = temp.replace(']','')
        temp = temp.replace("'",'')
        db.writelines(temp + '\n')
           
    #first = kegg.readline()
    #second = kegg.readline()
    #third = kegg.readline()
    #full = second.split()
    #temp = full[1]
    #temp = re.sub(rem,'',temp)
    message = "IF USING EXCEL TO VIEW KEGG FILE, EXAMINE ALL CYP*** WITH E (EX. 3E1)."+"\n"+ "IT WILL CONVERT TO NUMERICAL VALUE!"
    print message
    db.close()            
                

    
