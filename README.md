# ADP_tools

Functions for working with Sontek ADP files generated by Current Surveyor program. Includes example files and notebook.

Once you have the ADP_tools module, follow these steps exactly:
- Import the T file as a Pandas dataframe using the function `t_reader(‘filename’)`
- Use the function `tfile_Qest()` with the new dataframe.
- Use the function `dis_reader()` with the DIS file. This will create a new dataframe that’s compatible with the other functions in ADP_tools.
Next, we have to calculate the discharge, or Qn using information from both the T and DIS files
- Use `Qnorm()` with the modified T file dataframe, modified DIS file dataframe, and then your sampling interval
- Example code (from [test_example_data.py](test_example_data.py))

'''
import ADP_tools as ADP

dis_file = 'example_data/ELK2206151355.DIS'
t_file = 'example_data/ELK2206151355.T'

df_dis = ADP.dis_reader(dis_file)
df_t = ADP.t_reader(t_file)

df_tQ = ADP.tfile_Qest(df_t)

df_Q = ADP.Qnorm(df_tQ,df_dis,5)
'''

Once you’ve followed all of these steps, you now have a single dataframe that tells you the velocity magnitude (V), ADP_heading, true water direction relative to ADP heading (TWD), the velocity of each depth cell relative to the cross section (V_cs), and the estimated discharge rate for that specific depth cell (Q_est). These tools also construct the dataframe in a way that is easily convertible to an xarray dataframe, where you can separated your profiles by bin depth and profile number to form colorplots of your cross sections.
