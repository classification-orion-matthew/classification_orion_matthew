'''
misc functions for working with the titanic and iris dbase
'''
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

# binning and value_counts: 
def value_counts(dataframe):
    for col in dataframe.drop(columns=('customer_id')):
        if np.issubdtype(dataframe[col].dtype, np.number) and dataframe[col].nunique() > 10:
            print(dataframe[col].value_counts(bins=10, sort=False))
        else: 
            print(dataframe[col].value_counts(sort=False))


def handle_missing_values(dataframe):
    return dataframe.assign(
        total_charges = dataframe.total_charges.dropna(0)
    )

def churn_num(dataframe):
    return dataframe.assign(
        churn = dataframe['churn'].map({'No': 0, 'Yes': 1})

    )

def tenure_year(dataframe):
    dataframe['tenure_year'] = (dataframe.tenure / 12).astype(int) + 1
    return dataframe

choices_lns = [2, 1, 0]
choices = [3, 2, 1, 0]




def conditional_encodes(df):
    conditions_secback = [
    (df['online_security'] == 'Yes') & (df['online_backup'] == 'Yes'),
    (df['online_security'] == 'No') & (df['online_backup'] == 'Yes'), 
    (df['online_security'] == 'Yes') & (df['online_backup'] == 'No'),
    (df['online_security'] == 'No') & (df['online_backup'] == 'No')
    ]

    conditions_strm = [
    (df['streaming_tv'] == 'Yes') & (df['streaming_movies'] == 'Yes'),
    (df['streaming_tv'] == 'No') & (df['streaming_movies'] == 'Yes'), 
    (df['streaming_tv'] == 'Yes') & (df['streaming_movies'] == 'No'),
    (df['streaming_tv'] == 'No') & (df['streaming_movies'] == 'No')
    ]

    conditions_pdep = [
    (df['partner'] == 'Yes') & (df['dependents'] == 'Yes'),
    (df['partner'] == 'No') & (df['dependents'] == 'Yes'), 
    (df['partner'] == 'Yes') & (df['dependents'] == 'No'),
    (df['partner'] == 'No') & (df['dependents'] == 'No')
    ]

    conditions_lns = [
    (df['phone_service'] == 'Yes') & (df['multiple_lines'] == 'Yes'),
    (df['phone_service'] == 'Yes') & (df['multiple_lines'] == 'No'),
    (df['phone_service'] == 'No') & (df['multiple_lines'] == 'No')
    ]

    df['multiple_lines'] = np.select(conditions_lns, choices_lns)
    df['household_type_id'] = np.select(conditions_pdep, choices)
    df['streaming_services'] = np.select(conditions_strm, choices)
    df['online_security_backup'] = np.select(conditions_secback, choices)
    return df

def encode_gender(df):
    encoder=LabelEncoder()
    encoder.fit(df.gender)
    return df.assign(gender_e = encoder.transform(df.gender))

def encode_tech(df):
    encoder=LabelEncoder()
    encoder.fit(df.tech_support)
    return df.assign(tech_support_e = encoder.transform(df.tech_support))

def encode_paperless(df):
    encoder=LabelEncoder()
    encoder.fit(df.paperless_billing)
    return df.assign(paperless_billing_e = encoder.transform(df.paperless_billing))

def encode_device_protection(df):
    encoder=LabelEncoder()
    encoder.fit(df.device_protection)
    return df.assign(device_protection_e = encoder.transform(df.device_protection))

def drop_cols(df):
    return df.drop(columns=(['customer_id', 'partner', 'dependents', 'phone_service',
    'multiple_lines', 'online_security', 'online_backup',
    'streaming_tv', 'gender','streaming_movies', 'contract_type',
    'internet_service_type', 'payment_type', 'tech_support', 'paperless_billing', 'device_protection']))

def prep_telco_data(df):
        return df.pipe(handle_missing_values)\
        .pipe(churn_num)\
        .pipe(tenure_year)\
        .pipe(conditional_encodes)\
        .pipe(encode_gender)\
        .pipe(encode_device_protection)\
        .pipe(encode_tech)\
        .pipe(encode_paperless)

