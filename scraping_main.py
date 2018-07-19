import requests
import sys
import csv
import os
import time
from sortingData import textTocsv
from handlingCsv  import cleanUpCsvFile

# SOMC proxy setting
proxy_dict = {
    "http": "http://proxy.global.sonyericsson.net:8080",
    "https": "http://proxy.global.sonyericsson.net:8080",
}

somc_proxy = input("Needs SOMC proxy setting? (y/n): ")
base_url = input("Enter URL: ")
if base_url == "":      # If no URL entered, then use default URL
    base_url = "https://www.smartphone-guide.net/comparison/"

if somc_proxy.upper() == 'Y':       # SOMC proxy setting
    req = requests.get(base_url, proxies=proxy_dict, timeout=10)
else:
    req = requests.get(base_url, timeout=10)
urlStr = base_url[-4:-1]

if req.status_code == 200:
    print("--- Web page information ---")
    for key, value in req.headers.items():
        print(key, ":", value)
    print("encoding =", req.encoding, type(req.encoding))
    print("-"*20)

    try:
        if not os.path.exists("./savedata"):
            os.mkdir("savedata")
            time.sleep(0.5)

        sourceFile = "./savedata/web_source_" + urlStr + ".txt"
        print("Saving web page source file...")
        fw = open(sourceFile, 'w', encoding=req.encoding)
        fw.write(req.text)
        print("First 100 bytes:{}, ... ,".format(req.text[:100]))
        fw.close()

        # Open source file as read mode
        fr = open(sourceFile, 'r', encoding="utf_8")    # for debug, fr = open("web_source_son_test.txt", 'r', encoding="utf_8")
        # Open csv file to write
        csvDataFile = "./savedata/web_data_pre_" + urlStr + ".csv"
        fwcsv = open(csvDataFile, 'w', encoding="shift_jis", newline="")
        csvWriter = csv.writer(fwcsv, lineterminator="\n")

    except OSError as e:
        print("OS Error :", e)
        sys.exit()      # quit the program
    except Exception as err:
        print("Unexpected error happened :", err)
        sys.exit()      # quit the program

    # Copy text source file to csv file
    textTocsv(fr, csvWriter)

    fr.close()
    fwcsv.close()

    # Clean up csv file
    cleanUpCsvFile(urlStr, csvDataFile)


else:
    print("status_code =", req.status_code)
    print("Check URL and try it again...")
