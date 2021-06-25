# AUTOGENERATED! DO NOT EDIT! File to edit: 01_wrangle.ipynb (unless otherwise specified).

__all__ = ['drop_low_uniqueness_cols', 'drop_low_std_cols']

# Cell
#export
import pandas as pd

# Cell


def drop_low_uniqueness_cols(df: pd.DataFrame, nunique_thold=0.05) -> pd.DataFrame:
    """Drop columns with a low number of unique values.

    ##### Parameters:
    - **df** `pd.DataFrame` A pandas dataframe.
    - **nunique_thold** `float` or `int` If a float then will drop cols with a uniqueness rate below `nunique_thold`, if is an int then will use counts instead.

    ##### Returns:
    - **df** `pd.DataFrame` A pandas dataframe.

    """

    if isinstance(nunique_thold, int):
        df = df.loc[:, df.nunique() > nunique_thold]
    elif isinstance(nunique_thold, float) and nunique_thold < 1.0 :
        df = df.loc[:, df.nunique() / len(df) > nunique_thold]
    return df

# Cell


def drop_low_std_cols(df: pd.DataFrame, std_thold=0.05) -> pd.DataFrame:
    """Drop columns with a low standard deviation value.

    ##### Parameters:
    - **df** `pd.DataFrame` A pandas dataframe.
    - **std_thold** `float` Standard deviation threshold for columns below which they will be dropped.

    ##### Returns:
    - **df** `pd.DataFrame` A pandas dataframe.

    """

    df = df.loc[:, df.std() > std_thold]
    return df