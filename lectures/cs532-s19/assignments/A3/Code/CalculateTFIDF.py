import csv
import math

idfDenominator = 991
idfNumerator = 0
with open("C:\\SearcTermResults\\basketball.csv") as allSearchResultsForBasketball:
    reader_SearchResultsForBasketball = csv.reader(allSearchResultsForBasketball, delimiter=',')
    for searchResultsDetails in reader_SearchResultsForBasketball:
        idfNumerator = idfNumerator + int(searchResultsDetails[1])

with open("C:\\TFIDF.csv", "w", newline='') as tfIdfFile:
    writer = csv.writer(tfIdfFile)
    currentData = ['URL','TF', 'IDF','IDFLogBase2','TFIDF','TFIDFLogBase2']
    writer.writerow(currentData)
    with open("C:\\SearcTermResults\\BasketballSearchterm10IdentifiedForFurtherProcessing.csv") as idfentifiedresultFile:
        csv_reader = csv.reader(idfentifiedresultFile, delimiter=',')
        tfNumerator = 0
        tfDenominator = 0    
        for row in csv_reader:        
            tfNumerator = row[1]
            fileName_ResponseText = "C:\\ProcessedText\\" + row[0]
            with open(fileName_ResponseText, 'r') as f:
                for line in f:
                    words = line.split()
                    tfDenominator =  tfDenominator + len(words)
            TF = int(tfNumerator)/tfDenominator
            IDF = idfNumerator/idfDenominator
            IDFlogbase2 = math.log(IDF,2)
            TfIdf = TF * IDF
            TfIdfBasedOnlogbase2 = TF * IDFlogbase2
            currentData =[row[0],str(TF),str(IDF),str(IDFlogbase2),str(TfIdf),str(TfIdfBasedOnlogbase2)]
            writer.writerow(currentData)
print('Completed')

    
