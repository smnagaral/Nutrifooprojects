from pyexcel_ods import get_data

#MyValues = [] #create an empty list
#values = ods.reader(open('Project5_CSV_file.ods', 'rb'), delimiter=' ')
#for row in values:
 # MyValues.append(row[5])

  #Print(MyValues)

from pyexcel_ods import get_data
data = get_data("Project5_CSV_file.ods")
import json
print(json.dumps(data))
