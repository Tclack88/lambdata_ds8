# lambdata\_ds8

A utility for automating common fixes to pandas dataframes


## installation:

A worked notebook example can be found [here](https://github.com/Tclack88/DS-Unit-3-Sprint-1-Software-Engineering/blob/master/assignment2_Testing_Improved_DataFrame.ipynb)

`pip install -i https://test.pypi.org/simple/ lambdata-tclack==0.1.4`



## use:

`from lambdata_tclack.df_utils import ImprovedDataFrame`

### Convert from pandas dataframe:

A dataframe can be converted into an "ImprovedDataFrame" object


```python
>>> import pandas as pd
>>> from lambdata_tclack.df_utils import ImprovedDataFrame
>>> df = pd.DataFrame({"FIRST":[1,2,3],"second column":[4,5,6]})
>>> idf = ImprovedDataFrame(df)
>>> type(df)
<class 'pandas.core.frame.DataFrame'>
>>> type(idf)
<class 'lambdata_tclack.df_utils.ImprovedDataFrame'>
```

### Use additional convenience methods:
While as this new object, the newer methods can be called on it, even chained:

```python
>>> df
   FIRST  second column
0      1              4
1      2              5
2      3              6
>>> idf.simplify_cols()
   first  second_column
0      1              4
1      2              5
2      3              6
>>> idf.add_col('Newest     Column ADDDED',[7,8,9]).simplify_cols()
   first  second_column  newest_column_addded
0      1              4                     7
1      2              5                     8
2      3              6                     9
```

### original pandas dataframe methods and attributes work as expected
All regular pandas dataframe methods will still work, df.shape, df.columns, df.head(), and so on:

``` python
>>> idf.head()
   first  second_column  newest_column_added
0      1              4                    7
1      2              5                    8
2      3              6                    9
>>> idf.columns
Index(['first', 'second_column', 'newest_column_added'], dtype='object')
>>> idf.shape
(3, 3)
```

## Testing
A df\_utils\_test.py has been included with a dummy dataframe for verification with pytest

pytest maybe installed with `pip3 install pytest`

checking for correct behavior is as simple as running `pytest` 

(NOTE: there may be a conflict for systems with python2 install, which pytest may default to, checking with `pytest --version` will indicate which python is being used. In any case, python3 can be forced with `python3 -m pytest`)
