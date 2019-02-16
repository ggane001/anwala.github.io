import urllib.request
import json
import csv

urlCounter = 0
def getCarbonDate(uri):
    try:
        getCarbonDateUrlPrefix = "http://localhost:8888/cd/"
        contents = urllib.request.urlopen(getCarbonDateUrlPrefix + uri).read()
        #print(contents)
        jsonContents = json.loads(contents)
        responseCarbonDate = jsonContents["estimated-creation-date"]
        print(responseCarbonDate)
        return responseCarbonDate
    except:        
        return "No Estimate Creation Date"

with open("C:\ListOfCarbonDates.csv", "w", newline='') as csvFileListOfMementosTemp:
    writer = csv.writer(csvFileListOfMementosTemp)
    currentData = ['URL','Estimate Creation Date']
    writer.writerow(currentData)
    for currentUrl in open("C:\ListOfUniqueUrls.txt", "r"):
        urlCounter = urlCounter + 1        
        currentCarbonDate = getCarbonDate(currentUrl)        
        currentData = [currentUrl,currentCarbonDate]
        writer.writerow(currentData)
        print(urlCounter)
csvFileListOfMementosTemp.close()
print("Completed")