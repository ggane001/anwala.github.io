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

        return netloc + path + optionalQuery
    except:
        print('Error uri:', uri)

    return ''

uniqueUrls = set()
output_file = open("C:\ListOfUniqueUrls.txt", "w")
for currentUrl in open("C:\ListOfUrlsExpandedInput.txt", "r"):
    currentCanonicalizedURI = canonicalizeURI(currentUrl)
    if currentCanonicalizedURI not in uniqueUrls:
        output_file.write(currentUrl)
        uniqueUrls.add(currentCanonicalizedURI)
output_file.close()