from bs4 import BeautifulSoup
import argparse
import csv

def main ():
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", help="html input file")
    parser.add_argument("--outfile", help="output of the csv file", default='parsed.csv')
    args = parser.parse_args()
    infile = args.infile
    outfile = args.outfile
    with open (infile) as fp:
        soup = BeautifulSoup (fp, "html.parser")
    fp.close()
    trade_table = soup.find_all("table")[1]
    trade_datum = []
    trade_data = []
    for tr in trade_table.find_all("tr"):
        # for td in tr.find_all ("td"):
        tds = tr.find_all ("td")

        if len(tds) ==10:
            #print (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text)
            trade_data.append (tds[0].text.strip())
            trade_data.append (tds[1].text.strip())
            trade_data.append (tds[2].text.strip())
            trade_data.append (tds[3].text.strip())
            trade_data.append (tds[4].text.strip())
            trade_data.append (tds[5].text.strip())
            trade_data.append (tds[6].text.strip())
            trade_data.append (tds[7].text.strip())
            trade_data.append (tds[8].text.strip())
            trade_data.append (tds[9].text.strip())
        else:
            #print (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text)
            trade_data.append (tds[0].text.strip())
            trade_data.append (tds[1].text.strip())
            trade_data.append (tds[2].text.strip())
            trade_data.append (tds[3].text.strip())
            trade_data.append (tds[4].text.strip())
            trade_data.append (tds[5].text.strip())
            trade_data.append (tds[6].text.strip())
            trade_data.append (tds[7].text.strip())
            trade_data.append (tds[8].text.strip())
            trade_data.append ("")
        # print "\n"
        trade_datum.append(trade_data)
        trade_data = []

    csv_datum = []
    csv_data = []
    isFound = False
    for data in trade_datum:
        if data[2] == "sell":
            csv_data.append (data[0])
            csv_data.append (data[1])
            csv_data.append (data[2])
            csv_data.append (data[3])
            csv_data.append (data[4])
            csv_data.append (data[5])
            csv_data.append (data[6])
            csv_data.append (data[7])
            for data2 in trade_datum:
                if data2[2] == "close" and data[3]==data2[3]:
                    csv_data.append (data2[1])
                    csv_data.append (data2[5])
                    csv_data.append (data2[2])
                    break
                elif data2[2] == "s/l" and data[3]==data2[3]:
                    csv_data.append (data2[1])
                    csv_data.append (data2[5])
                    csv_data.append (data2[2])
                    break
                elif data2[2] == "t/p" and data[3]==data2[3]:
                    csv_data.append (data2[1])
                    csv_data.append (data2[5])
                    csv_data.append (data2[2])
                    break
                elif data2[2] == "close at stop" and data[3]==data2[3]:
                    csv_data.append (data2[1])
                    csv_data.append (data2[5])
                    csv_data.append (data2[2])
                    break
            csv_datum.append (csv_data)
            csv_data = []
        elif data[2] == "buy":
            csv_data.append (data[0])
            csv_data.append (data[1])
            csv_data.append (data[2])
            csv_data.append (data[3])
            csv_data.append (data[4])
            csv_data.append (data[5])
            csv_data.append (data[6])
            csv_data.append (data[7])
            for data2 in trade_datum:
                if data2[2] == "close" and data[3]==data2[3]:
                    csv_data.append (data2[1])
                    csv_data.append (data2[5])
                    csv_data.append (data2[2])
                    break
                elif data2[2] == "s/l" and data[3]==data2[3]:
                    csv_data.append (data2[1])
                    csv_data.append (data2[5])
                    csv_data.append (data2[2])
                    break
                elif data2[2] == "t/p" and data[3]==data2[3]:
                    csv_data.append (data2[1])
                    csv_data.append (data2[5])
                    csv_data.append (data2[2])
                    break
                elif data2[2] == "close at stop" and data[3]==data2[3]:
                    csv_data.append (data2[1])
                    csv_data.append (data2[5])
                    csv_data.append (data2[2])
                    break
            csv_datum.append (csv_data)
            csv_data = []

    with open (outfile, "wb") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow (["no","entry time","order type","order no", "size", "entry price", "stop loss", "take profit", "close time", "close price","close type"])
        for csv_data in csv_datum:
            csvwriter.writerow (csv_data)
    csvfile.close()
    print "Data extraction and conversion is finished."

if __name__ == "__main__":
    main()
