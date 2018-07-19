import csv
from handlingTags import removeTags

def textTocsv(fr, csvWriter):

    tableBegin = "<table"
    tableEnd = "</table>"
    tRowBegin = "<tr>"
    tRowEnd = "</tr>"
    tHeadBegin = "<th"
    #tHeadEnd = "</th>"
    #tDataBegin = "<td>"
    #tDataEnd = "</td>"
    breakPoint = "</html>"

    csv_list = []

    while True:
        line = fr.readline()
        line = line.strip()     # delete whitespaces from both top and bottom

        if tableBegin in line:  # handling inside a table
            while True:
                line = fr.readline()
                line = line.strip()     # delete whitespaces from both top and bottom

                if tableEnd in line:    # </table> end of table
                    csv_list.clear()
                    break
                elif (tRowEnd in line) and (tRowBegin in line): # </tr><tr> write current contents and clear it for next row
                    csvWriter.writerow(csv_list)
                    csv_list.clear()
                elif (tHeadBegin in line) and (tRowBegin in line): # this is actually patch work in case header <th and row begin <tr> are in the same line
                    csv_list.clear()
                    item = removeTags(line)
                    if "\u200f" in item:
                        item = item.replace("\u200f", " ")  # exception handling
                    if "\uff5e" in item:
                        item = item.replace("\uff5e", " ")  # exception handling
                    if "\u2014" in item:
                        item = item.replace("\u2014", " ")  # exception handling
                    csv_list.append(item)
                    csvWriter.writerow(csv_list)
                    csv_list.clear()
                elif tRowBegin in line:     # <tr> start new table row, then clear the list
                    csv_list.clear()
                elif tRowEnd in line:       # </tr> end of table row, then write to csv
                    csvWriter.writerow(csv_list)
                else:
                    item = removeTags(line)
                    if "\u200f" in item:
                        item = item.replace("\u200f", " ")  # exception handling
                    if "\uff5e" in item:
                        item = item.replace("\uff5e", " ")  # exception handling
                    if "\u2014" in item:
                        item = item.replace("\u2014", " ")  # exception handling
                    if "\u2013" in item:
                        item = item.replace("\u2013", " ")  # exception handling
                    #if item != "":
                    csv_list.append(item)
        elif breakPoint in line:
            break
        else:
            item = removeTags(line)
            if item != "":
                if "\u200f" in item:
                    item = item.replace("\u200f", " ")  # exception handling
                if "\uff5e" in item:
                    item = item.replace("\uff5e", " ")  # exception handling
                if "\xa0" in item:
                    item = item.replace("\xa0", " ")  # exception handling
                csv_list.append(item)
            csvWriter.writerow(csv_list)
            csv_list.clear()
