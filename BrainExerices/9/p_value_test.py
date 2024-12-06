import pandas as pd
import numpy as np

file_path = 'brain_excer.csv'
data = pd.read_csv(file_path)

data['delta'] = np.log(data['L1']) - np.log(data['L0'])

p_value = (data['delta'] <= 0).mean()

print(p_value)
