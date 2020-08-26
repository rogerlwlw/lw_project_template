:mod:`project_lib.dataset.load_data`
====================================

.. py:module:: project_lib.dataset.load_data

.. autoapi-nested-parse::

   The :mod:`load_data` module offers function to load 'data'
   in 'dataset/data' folder, supported formats are
   ['.csv', '.xlsx', '.pkl']. By dault a DataFrame object will be returned.
   The DataFrame should have a column labled as 'y' as the target class

   Created on Tue Dec 10 17:42:49 2019

   @author: roger luo



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   project_lib.dataset.load_data.get_local_data


.. function:: get_local_data(data_name=None, all_datafile=False, rel_path=None)

   read data file by filename from `data` folder, extension suffix included

   data_name :
       file name of data to be loaded, by default stored as .csv in 'data'
       folder, suffix must be included

   all_datafile : bool
       if all_datafile=True then, load all file in 'data' folder;

   rel_path :
       subfoler of 'data' folder to search from, default None will search all
       folders recursively

   Return :
       if data_name=None, then return list of filename that could  be loaded
       if data_name is not None, then load that data with 'data_name'


