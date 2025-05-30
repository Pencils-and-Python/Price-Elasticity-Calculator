"""db/register.py"""

def register_dataframes(train_df, store_df, con):
    con.register("train_df", train_df)
    con.register("store_df", store_df)
