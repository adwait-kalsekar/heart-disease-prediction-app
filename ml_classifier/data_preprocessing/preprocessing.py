import pandas as pd
import joblib

def load_model_data():
    model = joblib.load("ml_classifier/trained_model/final_model.pkl")
    col_names = joblib.load("ml_classifier/trained_model/col_names.pkl")

    return model, col_names

def convert_to_int(df, column_names):
    for column_name in column_names:
        df[column_name] = df[column_name].astype(str).astype(int)
    return df

def encode_data(df):
    column_names = joblib.load("ml_classifier/trained_model/col_names.pkl")
    encoded_df = convert_to_int(df, column_names)
    
    # df_object_type = df.select_dtypes(include='object')

    # df_numeric_type = df.select_dtypes(exclude='object')

    # df_object_dummies = dummy_data(df_object_type)

    # encoded_df = pd.concat([df_numeric_type, df_object_dummies], axis=1)

    return encoded_df