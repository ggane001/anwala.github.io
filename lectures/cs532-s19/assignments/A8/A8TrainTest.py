import os
from subprocess import check_output

cl = docclass.naivebayes(docclass.getwords)

dbfile = 'anwala.db'

if( os.path.exists(dbfile) ):
    check_output(['rm', dbfile])
    print('removed dbfile:', dbfile)

cl.setdb(dbfile)
docclass.spamTrain(cl)
docclass.notSpamTrain(cl)

for x in range(11):
    if(x != 0):
        fileTemp = "C:\\Mails\\Testing\\S\\Testing "+ str(x) +".txt"
        with open(fileTemp, "r") as file:            
            data = file.read()
            print(cl.classify(data))

for x in range(11):
    if(x != 0):
        fileTemp = "C:\\Mails\\Testing\\NS\Testing "+ str(x) +".txt"
        with open(fileTemp, "r") as file:            
            data = file.read()
            print(cl.classify(data))






