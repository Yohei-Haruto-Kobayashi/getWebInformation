import csv

def cleanUpCsvFile(urlStr, csvDataFile):
    frd = open(csvDataFile, 'r')
    csvReader = csv.reader(frd)

    csvWriteFile = "./savedata/web_data_" + urlStr + ".csv"
    fwr = open(csvWriteFile, 'w', encoding="shift_jis", newline="")
    csvWriter = csv.writer(fwr)
    w_list = []

    for row in csvReader:       # read data line by line
        try:
            if row[0] == "":    # if first item in a line is empty
                continue
        except IndexError as e:
            print("handling csv file,", e)
            continue

        for item in row:
            start = item.find('<')
            stop = item.find('>')
            count = 0
            while (start != -1) and (stop != -1) and (count < 20):
                item = item[0:start] + item[stop+1:]
                start = item.find('<')
                stop = item.find('>')
                count += 1
            w_list.append(item)
        csvWriter.writerow(w_list)      # write one line
        w_list.clear()

    frd.close()
    fwr.close()
