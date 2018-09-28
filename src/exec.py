import pandas as pd
import time
import src.topDown_ed as topdown_ed
import src.recursive_ed as recursive_ed
import src.bottomUp_ed as botomup_ed


df = pd.read_csv('cases.csv',index_col=0)
print (df)

for i,row in df.iterrows():
	print('----')
	x = row['x']
	y = row['y']
	print ('x :', x)
	print ('y :', y)
	res, exec_time = recursive_ed.run_recursive_ed(x,y)
	print('Recursive' ,res, exec_time)
	res, exec_time = topdown_ed.run_topdown_ed(x,y)
	print('Top Down' ,res, exec_time)
	res, exec_time , _= botomup_ed.run_bottomup_ed(x,y)
	print('Bottom up' , res, exec_time)