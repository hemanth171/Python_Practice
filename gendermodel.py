import pandas as pd
import csv as csv

filename = '/Users/hemanth/Documents/Python_workspace/test.csv'

data_frame = pd.read_csv(filename)
data = data_frame.as_matrix(columns=None)

prediction_file = open('/Users/hemanth/Documents/Python_workspace/genderbasedmodel.csv', 'wb')
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(['PassengerId', 'Survived'])
for row in data:
    if row[3] == 'female':
        prediction_file_object.writerow([row[0], '1'])
    else:
        prediction_file_object.writerow([row[0], '0'])

prediction_file.close()