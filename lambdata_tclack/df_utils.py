import pandas as pd

def simplify_cols(df):
    """
    for pandas dataframe columns:
    replace spaces with underscores and changes everything to lowercase
    This allows for dot notation. As a side effect, mutiple spaces get 
    reduced to one, and leading/triling spaces are removed entirely
    """
    old_cols = list(df.columns)
    new_cols = ['_'.join(col.lower().split()) for col in old_cols]
    rename = dict(zip(old_cols,new_cols))
    return df.rename(columns=rename)



def add_col(df,name,new_list):
    """
    Adds new column to a dataframe from list format.
    Checks for size compatibility warns if not
    """
    assert len(new_list) == df.shape[0],'list size not compatible with dataframe size'
    df[name] = pd.Series(new_list)
    return df
