import json
import csv
myList = []
jsonfile = open('Project5_Json_file.json', 'w')
with open('Project5_CSV_file.csv', newline='') as csvfile:
    #spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fieldnames = ("Number","Name","Ability")
    reader = csv.DictReader( csvfile, fieldnames)
    for row in reader:
    	myList.append(row)
    	#out = json.dumps(row)
    	#jsonfile.write(out)
    for i in range(0,5):
    	print(myList[i])
    	json.dump(myList[i], jsonfile)
    	jsonfile.write('\n')

jsonfile.close()


