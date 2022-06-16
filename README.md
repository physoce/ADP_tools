# ADP_tools

Functions for working with Sontek ADP files generated by Current Surveyor program. Includes example files and notebook.

Once you have the ADP_tools module, follow these steps exactly:
- Import the T file as a Pandas dataframe using the function `t_reader(‘filename’)`
- Use the function `tfile_Qest()` with the new dataframe and call it by the same name
- Export this new dataframe as a csv to the folder of your choice
Next, you have to go into the DIS file and change the orientation of some things. Below is a transcript of how it should look:

```
% ADP Data File: ELK2205021146.adp
% Start Date + Time: 02/05/2022 11:46:25
% All Track Calculations use: Bottom Track data
% All Flow Velocities Relative to: Bottom Track
% Metric Units
Profile   Time   Distance(m)      DMG(m)  DistEast(m) DistNorth(m) Latitude(deg) Longitude(deg) Depth_1(m) Depth_2(m) Depth_3(m) AvDepth(m) EsDepth(m)  uVess(m/s) DirVess(deg)  uFlow(m/s) DirFlow(deg)  StdDev(m/s) DQI #_Valid_Cells      Q(m^3/s)      Q_Cumul(m^3/s)

      1 11 46 25      1.6      1.6     -0.8      1.4    36.81242167  -121.78180167   4.03   3.85   3.31   3.73    0.00    0.32   331.3   0.32   323.1    0.02   1.0      5       0.27        0.3   0.00
      2 11 46 30      4.2      3.8      0.3      3.8    36.81241833  -121.78178333   4.27   3.79   3.60   3.89    0.00    0.51    23.9   0.40     5.8    0.01   0.8      6       1.23        1.5   0.00
%-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
%
% Discharge Summary
% 
% Top Q      = 30.978 (cms)
% Measured Q = 119.24 (cms)
% Bottom Q   = 28.279 (cms)
% Left Q     = 0.00000 (cms)
% Right Q    = 0.00000 (cms)
% Total Q    = 178.49 (cms)
% 
% MeasQ/EstQ = 66.8 (%)
% 
% TotalArea  = 707.17 (m2)
% MeanVel    = 0.25 (m/s)
```

Of course, you’ll have more lines of data, but the important things is the name of the columns and removing the text dividers.
- Use the function `dis_reader()` with your modified DIS file as a CSV
- This will create a new dataframe with the modified DIS file that’s compatible with the other functions in ADP_tools
Next, we have to calculate the discharge, or Qn using information from both the T and DIS files
- Use `Qnorm()` with the modified T file dataframe, modified DIS file dataframe, and then your sampling interval
- EX: `dfQnorm = Qnorm(Tfile_df, DISfile_df, 5)`

Once you’ve followed all of these steps, you now have a single dataframe that tells you the velocity magnitude (V), ADP_heading, true water direction relative to ADP heading (TWD), the velocity of each depth cell relative to the cross section (V_cs), and the estimated discharge rate for that specific depth cell (Q_est). These tools also construct the dataframe in a way that is easily convertible to an xarray dataframe, where you can separated your profiles by bin depth and profile number to form colorplots of your cross sections.