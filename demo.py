import pandas as pd
a=pd.DataFrame({"A":[4,5,6],"B":[7,8,9],"C":[10,11,12]},index=pd.MultiIndex.from_tuples([('d',1),('d',2),('e',2)],names=['N','V']))
print(a)