import pandas as pd
import numpy as np

filename = '/Users/hemanth/Documents/Python_workspace/train.csv'
data_frame = pd.read_csv(filename)

data = data_frame.as_matrix(columns=None)

number_passengers = np.size(data[0:, 1].astype(np.float))
number_survived = np.sum(data[0:, 1].astype(np.float))
proportion_survived = number_survived/ number_passengers

women_only_stats = data[0:, 4] == 'female'
men_only_stats = data[0:, 4] != 'female'

women_onboard = data[women_only_stats, 1].astype(np.float)
men_onboard = data[men_only_stats, 1].astype(np.float)
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)
print 'Proportion of women who survived is %s' %proportion_women_survived
print 'Proportion of men who survived is %s' %proportion_men_survived