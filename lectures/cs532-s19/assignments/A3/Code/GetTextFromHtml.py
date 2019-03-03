from boilerpipe.extract import Extractor
from urllib.parse import urlparse
import glob   
import os

path = 'C:\\RawHtmls/*.txt' 
urlCounter = 0
files=glob.glob(path)   
for file in files:  
    try:
        urlCounter = urlCounter + 1
        f=open(file, 'r')  
        fileName = fileName = "C:\\ProcessedText\\" + os.path.basename(f.name)
        currentHtml = f.read()
        f.close()
        extractor = Extractor(extractor='ArticleExtractor', html=currentHtml)
        currentText = extractor.getText()
        output_file = open(fileName, "w")
        output_file.write(str(currentText.encode("utf-8")))
        output_file.close()
        print("Download Completed : " + fileName)
    except:
        print('Error :', urlCounter)