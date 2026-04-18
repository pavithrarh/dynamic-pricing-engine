import pandas as pd
from sklearn.preprocessing import LabelEncoder

le_product = LabelEncoder()
le_season = LabelEncoder()

def preprocess(df):
    df['product_type'] = le_product.fit_transform(df['product_type'])
    df['season'] = le_season.fit_transform(df['season'])
    return df