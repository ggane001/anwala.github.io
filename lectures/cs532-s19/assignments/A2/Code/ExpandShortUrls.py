import urllib.request

listOfUrlsFile = open("C:\ListOfUrls.txt", "r")
fileToStoreListOfUrlsExpanded = open("C:\ListOfUrlsExpanded.txt","a+")
for currentUrl in listOfUrlsFile:
    try:
        with urllib.request.urlopen(currentUrl) as url:        
            currentExpandedUrl = url.geturl()
            fileToStoreListOfUrlsExpanded.write(currentExpandedUrl + '\n')
    except:
        pass
listOfUrlsFile.close()
fileToStoreListOfUrlsExpanded.close()