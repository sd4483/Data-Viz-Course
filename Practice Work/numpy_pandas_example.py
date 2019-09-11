import numpy as np
import pandas as pd

sud_mat = np.arange(0,10).reshape(5,2)
#print(sud_mat)
sud_cols = ['A','B']
sud_idx = [['V','W','X','Y','Z']]
df=pd.DataFrame(data=sud_mat, columns=sud_cols, index=sud_idx)
print(df)
