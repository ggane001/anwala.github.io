import urllib.request
import json
import csv

urlCounter = 0
def getTimeMapAndMomentos(uri,currentUrlLineCounter):
    try:
        currentfileName = "C:\Timegate\\" + str(currentUrlLineCounter) + ".txt"
        output_file = open(currentfileName , "w")
        memgatorJsonRequestUrlPrefix = "https://memgator.cs.odu.edu/timemap/json/"
        contents = urllib.request.urlopen(memgatorJsonRequestUrlPrefix + uri).read()
        #print(contents)
        jsonContents = json.loads(contents)
        output_file.write(str(contents))
        output_file.close()
        mementosCount = len(jsonContents["mementos"]["list"])
        return mementosCount
    except:        
        return 0

with open("C:\ListOfMementos.csv", "w", newline='') as csvFileListOfMementosTemp:
    writer = csv.writer(csvFileListOfMementosTemp)
    currentData = ['URL','MementosCount']
    writer.writerow(currentData)
    for currentUrl in open("C:\ListOfUniqueUrls.txt", "r"):
        urlCounter = urlCounter + 1        
        currentMementosCount = getTimeMapAndMomentos(currentUrl,urlCounter)        
        currentData = [currentUrl,currentMementosCount]
        writer.writerow(currentData)
        print(urlCounter)
csvFileListOfMementosTemp.close()
print("Completed.")