import json
import csv
myList = []
def fileWrite():
    jsonfile = open('Project5_Json_file.json', 'w')
    return jsonfile

    #spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
def reader():
    with open('Project5_CSV_file.csv', newline='') as csvfile:
        fieldnames = ("Number","Name","Ability")
        reader1 = csv.DictReader( csvfile, fieldnames)
        for row in reader1:
            myList.append(row)
    	#out = json.dumps(row)
    	#jsonfile.write(out)
def write():
    jsonfile = fileWrite()
    for i in range(0,5):
        print(myList[i])
        json.dump(myList[i], jsonfile)
        jsonfile.write('\n')
    jsonfile.close()
reader()
write()