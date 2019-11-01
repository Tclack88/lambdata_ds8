import pandas as pd
from df_utils import ImprovedDataFrame
from __init__ import flatten
import base64

df = pd.DataFrame({'FIRST':[1,2,3],'Column 2': [4,5,6]})

idf = ImprovedDataFrame(df) 

def test_columns():
    idf_cols = idf.simplify_cols()
    for col in idf_cols:
        assert col.lower() == col,"uppercase present in column name"
        assert ' ' not in col,"spaces present in column name"

def test_entries():
    idf_simple = idf.correctify()
    unique_col_entries = pd.unique(idf_simple.values.ravel())
    assert len(unique_col_entries) == 1,"multiple entries exist"
    assert unique_col_entries[0] == "Mikayla Smells","Mikayla does not Smell!"

