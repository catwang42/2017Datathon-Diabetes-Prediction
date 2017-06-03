#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:07:18 2017

@author: zhizhenwang
"""

import pandas as pd
import os
import numpy as np 

#load prep data 
transClean = pd.read_csv('/Users/zhizhenwang/Desktop/2017Datathon/Datathon 2017/clean/5_xgb_model.gz', compression='gzip')


x = transClean[(transClean['Dispense_Week'] <= "2016-01-01") & (transClean['ChronicIllness'].str.contains('Diabetes'))]
lstTrans = pd.to_datetime(max(transClean.Dispense_Week))
del transClean

# replace NaN with NA
# DataFrame.fillna('NA')


# 1. Kurt/Skew of drug qty -----------------------------------------------
x['Dispense_Week'] = pd.to_numeric(x['Dispense_Week'])
illSkew= x.groupby('Patient_ID')['Dispense_WeekNum'].skew()


