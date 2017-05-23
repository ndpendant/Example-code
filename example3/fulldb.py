import csv


if __name__ == "__main__":
    
    drugbankdb = "C:\Users\dekai\Desktop\USF Database\Drugbank.csv"
    supercypdb = "C:\Users\dekai\Desktop\USF Database\supercyp.csv"
    indianadb = "C:\Users\dekai\Desktop\USF Database\Indiana.csv"
    keggdb = "C:\Users\dekai\Desktop\USF Database\kegg.csv"
    ildcaredb = "C:\Users\dekai\Desktop\USF Database\ildcare.csv"
    db = open("C:\Users\dekai\Desktop\USF Database\db.csv",'wb')
    fdb = csv.writer(db,delimiter=",")
    fulldb = []
    cypids =["1A1","1A2","1B1","2A6","2A13"
,"2B6"
,"2C8"
,"2C9"
,"2C11"
,"2C18"
,"2C19"
,"2D6"
,"2E1"
,"2F1"
,"2J2"
,"2S1"
,"2W1"
,"3A"
,"3A4"
,"3A5"
,"3A7"
,"3A43"
,"4A11"
,"4B1"
,"4F2"
,"4F3"
,"4F8"
,"4F11"
,"4F12"
,"4F22"
,"5A1"
,"7A1"
,"7B1"
,"8A1"
,"8B1"
,"11A"
,"11B1"
,"11B2"
,"17A"
,"19A"
,"21A"
,"24A"
,"26A1"
,"26B"
,"27A"
,"27B"
,"39A"
,"46A"
,"51A"
,"17"
,"D05987"
,"excretion"
,"nocyp"
,"P450"
,"not known"]
    
    header=["Drug", "CYP***", "Action","Species", "Database","refence_1", "reference_2","reference_3","Strength"]
    fdb.writerow(header)
    for i in cypids:
        opendrugbankdb = open(drugbankdb,'r')
        opensupercypdb= open(supercypdb,'r')
        openindianadb = open(indianadb,'r')
        openildcaredb = open(ildcaredb,'r')
        openkeggdb = open(keggdb,'r')
        drugbank=[]
        supercyp=[]
        indiana=[]
        ildcare=[]
        kegg=[]
        
        for line in opendrugbankdb:
            if i in line:
                drugbank.append(line)
        for line in opensupercypdb:
            if i in line:
                supercyp.append(line)
        for line in openindianadb:
           if i in line:
               indiana.append(line)
        for line in openildcaredb:
            if i in line:
                ildcare.append(line)
        for line in openkeggdb:
            if i in line:
                kegg.append(line)
        fulldb.append(drugbank)
        fulldb.append(supercyp)
        fulldb.append(indiana)
        fulldb.append(kegg)
        fulldb.append(ildcare)
        opendrugbankdb.close()
        openindianadb.close()
        opensupercypdb.close()
        openildcaredb.close()
        openkeggdb.close()
        
    for i in fulldb:
        db.writelines(i)
    
    db.close()
