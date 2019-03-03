import glob   
import os
import csv
import re

searchString = "music"
path = 'C:\\ProcessedText/*.txt' 
output_file_name = "C:\\SearcTermResults\\" + searchString +".csv"
with open(output_file_name, "w", newline='') as output_file:
    writer = csv.writer(output_file)
    files=glob.glob(path)   
    for file in files:  
        #try:        
        f=open(file, 'r')
        fileName = os.path.basename(f.name)
        print(fileName)
        hit_count = 0
        regexSearch = "(.*)(" + searchString + ")(.*)"
        for line in f:
            if re.match(regexSearch, line):
                currenthit_count = line.count(searchString)
                hit_count = hit_count + currenthit_count 
        f.close()
        currentData = [fileName,str(hit_count)]
        writer.writerow(currentData)            
        #except:
        #    print('Error :', fileName)
    #print("Search Completed : " + fileName)
output_file.close()
print("Search Completed!")