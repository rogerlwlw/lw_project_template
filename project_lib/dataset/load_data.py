# -*- coding: utf-8 -*-
"""
1)load datafile in dataset module under 'data' folder.

2)by dault a DataFrame object will be loaded.

3)the datafile should be 2D matrix with 'y' label as the target label, supported
format are ['.csv', '.xlsx', '.pkl']

Created on Tue Dec 10 17:42:49 2019

@author: roger luo
"""

import inspect
import os

from lw_mlearn.utilis.read_write import Objs_management

file_path = os.path.split(inspect.currentframe().f_code.co_filename)[0]
data_path = os.path.join(file_path, 'data')


def get_local_data(data_name=None, all_datafile=False, rel_path=None):
    '''return data as DataFrame 
    
    data_name:
        file name of data to be loaded, by default stored as .csv in 'data' 
        folder, suffix of file must be given
    rel_path:
        subfoler of 'data' folder to search from, default None will search all
        
    return
    ----
        if all_datafile is True then, load all file in 'data' folder
        else:
            if data_name is None, then return list of filename that could 
            be loaded
            if data_name is not None, then load that datafile
    '''
    reader = Objs_management(data_path)
    if all_datafile is True:
        lst, _ = reader.read_all(path=rel_path,
                                 suffix=['.csv', '.xlsx', '.pkl'],
                                 subfolder=True)
        return lst

    available_files = reader.list_all(path=rel_path,
                                      suffix=['.csv', '.xlsx', '.pkl'],
                                      subfolder=True)
    if data_name is None:
        return available_files.keys()
    else:
        file_name = available_files.get(data_name)
        if file_name is None:
            raise ValueError(
                "data file '{}' not found \n available files: {}".format(
                    data_name, available_files.keys()))
        return reader.read(file_name)


def _remove_label(df):
    ''' remove column labels of dataframe to make data uninterpretable
    also encode categories as C + 'integer'
    
    target classification label must be 'y'
    '''
    import pandas as pd
    import numpy as np
    from pandas.core.dtypes import api
    from lw_mlearn.utilis.utilis import to_num_datetime_df

    def _mapping_col(col, na_values=['null', '缺失值', -999, -99999, -1]):
        ''' encrypt categorical features
        '''
        col = col.replace(na_values, np.nan)
        if not api.is_numeric_dtype(col):
            uniq = col.unique()
            mapper = dict(
                zip(uniq, [''.join(['C', str(i)]) for i in range(len(uniq))]))

            if mapper.get(np.nan) is not None:
                mapper.pop(np.nan)

            col = col.map(mapper, na_action='ignore')

        return col

    df = to_num_datetime_df(df)
    y = df.pop('y')

    # encrypt categorical features
    X = df.apply(_mapping_col, axis=0)
    # remove column labels
    X = pd.DataFrame(X.values)

    X['y'] = y
    return X


if __name__ == '__main__':
    df = get_local_data('loan_short.csv')
#    df.to_csv('mushrooms.csv', index=False)
#    df2 = _remove_label(df)
#    df2.to_csv('loan_credit2.csv', index=False)
