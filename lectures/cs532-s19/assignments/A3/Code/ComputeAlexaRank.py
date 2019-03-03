import urllib, sys, bs4, csv
with open("C:\RankAlexa.csv", "w", newline='') as csvFileRankAlexa:
    writer = csv.writer(csvFileRankAlexa)
    currentData = ['URL','AlexaPageRank']
    writer.writerow(currentData)
    with open("C:\InputForAlexa.csv") as inputForKendallTau_b:
        reader_inputForKendallTau_b = csv.reader(inputForKendallTau_b, delimiter=',')
        next(reader_inputForKendallTau_b)
        for row in reader_inputForKendallTau_b:
            try:
                xml = urllib.request.urlopen('http://data.alexa.com/data?cli=10&dat=snbamz&url=s'+ row[0]).read()
                rank = bs4.BeautifulSoup(xml, "xml").find("REACH")['RANK']
                currentData = [row[0],rank]
                writer.writerow(currentData)
            except:
                print('Rank not found for ' + row[0])