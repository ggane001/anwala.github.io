import urllib.request
import json
import csv
from urllib.parse import urlparse

urlCounter = 0

for currentUrl in open("C:\ListOfUniqueUrls.txt", "r"):
    try:
        urlCounter = urlCounter + 1
        with urllib.request.urlopen(currentUrl) as res: 
            currentHtml = res.read()
            parsed_uri = urlparse(currentUrl)
            fileName = "C:\\RawHtmls\\" + str(urlCounter) + "_" + parsed_uri.netloc + ".txt"
            output_file = open(fileName, "w")
            output_file.write(str(currentHtml))
            output_file.close()
            print("Download Completed : " + fileName)
    except:
        print('Error :', currentUrl)