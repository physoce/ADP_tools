'''
Run code with example data
'''

import pandas as pd
import ADP_tools as ADP

dis_file = 'example_data/ELK2206151355.DIS'
t_file = 'example_data/ELK2206151355.T'

df_dis = ADP.dis_reader(dis_file)
df_t = ADP.t_reader(t_file)

df_tQ = ADP.tfile_Qest(df_t)

df_Q = ADP.Qnorm(df_tQ,df_dis,5)