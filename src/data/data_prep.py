import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"A": [1,2,3,4,5], "B": [6,7,8,9,10]})
print(df) 

df2 = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])