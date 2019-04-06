from googlesearch import search 
import csv
from urllib.parse import urlparse
import hashlib

def canonicalizeURI(uri):
    uri = uri.strip()
    if( len(uri) == 0 ):
        return ''
    exceptionDomains = ['www.youtube.com']
    try:
        scheme, netloc, path, params, query, fragment = urlparse( uri )
        netloc = netloc.strip()
        path = path.strip()
        optionalQuery = ''

        if( len(path) != 0 ):
            if( path[-1] != '/' ):
                path = path + '/'

        if( netloc in exceptionDomains ):
            optionalQuery = query.strip()

        return netloc
    except:
        print('Error uri:', uri)

    return ''

query = "site:blogspot.com  music review"
uniqueUrls = set()
counter1 = 0
with open("C:\\Q61UriListBlogspot.csv", "w", newline='') as csvFile:
    writer = csv.writer(csvFile)
    currentData = ['http://f-measure.blogspot.com/']
    #print(currentData)
    writer.writerow(currentData)
    for j in search(query, tld="com", num=49, stop=200, pause=3):   
        currentCanonicalizedURI = canonicalizeURI(j)
        if currentCanonicalizedURI not in uniqueUrls:
            currentData = [j]
            writer.writerow(currentData)
            uniqueUrls.add(currentCanonicalizedURI)
            print(j)
            counter1 = counter1 + 1
            if(counter1 > 49):
                break