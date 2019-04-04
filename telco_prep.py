'''
misc functions for working with the titanic and iris dbase
'''
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler


def peekatdata(df):
    '''gives cursory sample of dataframe passed'''
    head_df = df.head(5)
    print(head_df)
    tail_df = df.tail(5)
    print(tail_df)
    shape_tuple = df.shape
    print(shape_tuple)
    describe_df = df.describe()
    print(describe_df)
    df.info()

# binning and value_counts: 
def value_counts(dataframe):
    ''' assesses numerical/continuous data in telco and bins if appropriate'''
    for col in dataframe.drop(columns=('customer_id')):
        if np.issubdtype(dataframe[col].dtype, np.number) and dataframe[col].nunique() > 10:
            print(dataframe[col].value_counts(bins=10, sort=False))
        else: 
            print(dataframe[col].value_counts(sort=False))


def handle_missing_values(dataframe):
    '''removes customers with total charges of 0, i.e. customers that haven't been with the company long
    enough to glean information about churn from as they just signed up (very small portion of dataset)'''
    return dataframe.assign(
        total_charges = dataframe.total_charges.dropna()
    )

def churn_num(dataframe):
    '''enumerates churn column from a yes/no to 0 or 1 for better analysis.  maps explicit values.'''
    return dataframe.assign(
        churn = dataframe['churn'].map({'No': 0, 'Yes': 1})

    )

def tenure_year(dataframe):
    '''creates a new column in telco dataframe called tenure_year that assesses what year of service a 
    customer is in at the time of snapshot'''
    dataframe['tenure_year'] = (dataframe.tenure / 12).astype(int) + 1
    return dataframe


def sort_int_service(df):
    '''re-orders our internet service type id into a new column for better correlative analysis
    no internet service is remapped to 0 and incrementing services ++ from there'''
    df['int_type_id'] = df['internet_service_type_id'].replace({3: 0, 2: 2, 1: 1})
    return df

# setting up choices for logical conditions in coming function: 
choices_lns = [2, 1, 0]
choices = [3, 2, 1, 0]





def conditional_encodes(df):
    '''creates four new columns for our dataset that enumerates values based on a combination of data
    from two separate columns into each new column'''

    # Combining online security service with online backup service:
    conditions_secback = [
    (df['online_security'] == 'Yes') & (df['online_backup'] == 'Yes'),
    (df['online_security'] == 'No') & (df['online_backup'] == 'Yes'), 
    (df['online_security'] == 'Yes') & (df['online_backup'] == 'No'),
    (df['online_security'] == 'No') & (df['online_backup'] == 'No')
    ]

    # Combining streaming tv service and streaming movie service:
    conditions_strm = [
    (df['streaming_tv'] == 'Yes') & (df['streaming_movies'] == 'Yes'),
    (df['streaming_tv'] == 'No') & (df['streaming_movies'] == 'Yes'), 
    (df['streaming_tv'] == 'Yes') & (df['streaming_movies'] == 'No'),
    (df['streaming_tv'] == 'No') & (df['streaming_movies'] == 'No')
    ]

    # Combining partner and dependents status in household:
    conditions_pdep = [
    (df['partner'] == 'Yes') & (df['dependents'] == 'Yes'),
    (df['partner'] == 'No') & (df['dependents'] == 'Yes'), 
    (df['partner'] == 'Yes') & (df['dependents'] == 'No'),
    (df['partner'] == 'No') & (df['dependents'] == 'No')
    ]

    # Combining phone service status with multiple phone line status:
    conditions_lns = [
    (df['phone_service'] == 'Yes') & (df['multiple_lines'] == 'Yes'),
    (df['phone_service'] == 'Yes') & (df['multiple_lines'] == 'No'),
    (df['phone_service'] == 'No') & (df['multiple_lines'] == 'No')
    ]
    # Implementing logical statements into new columns utilizing numpy select:
    df['phone_id'] = np.select(conditions_lns, choices_lns)
    df['household_type_id'] = np.select(conditions_pdep, choices)
    df['streaming_services'] = np.select(conditions_strm, choices)
    df['online_security_backup'] = np.select(conditions_secback, choices)
    return df

def encode_gender(df):
    '''encodes gender column into a new enumerated column'''
    encoder=LabelEncoder()
    encoder.fit(df.gender)
    return df.assign(gender_e = encoder.transform(df.gender))

def encode_tech(df):
    '''encodes tech support column into a new enumerated column'''
    encoder=LabelEncoder()
    encoder.fit(df.tech_support)
    return df.assign(tech_support_e = encoder.transform(df.tech_support))

def encode_paperless(df):
    '''encodes paperless billing column into new enumerated column'''
    encoder=LabelEncoder()
    encoder.fit(df.paperless_billing)
    return df.assign(paperless_billing_e = encoder.transform(df.paperless_billing))

def encode_device_protection(df):
    '''encodes device protection column into new enumerated column'''
    encoder=LabelEncoder()
    encoder.fit(df.device_protection)
    return df.assign(device_protection_e = encoder.transform(df.device_protection))

def format_totals(df):
    '''formats total charges from a string object to a numeric type'''
    df['total_charges'] = df['total_charges'].convert_objects(convert_numeric=True)
    df = df[pd.notna(df.total_charges)]
    return df

def drop_cols(df):
    '''drops customer_id and non-numeric versions of existing columns for exploratory analysis purposes'''
    return df.drop(columns=(['customer_id', 'partner', 'dependents', 'phone_service',
    'multiple_lines', 'online_security', 'online_backup',
    'streaming_tv', 'gender','streaming_movies', 'contract_type',
    'internet_service_type', 'internet_service_type_id', 'payment_type', 'tech_support', 'paperless_billing', 'device_protection']))

def prep_telco_data(df):
    '''pipes all but drop_cols and value_counts to groom our initial dataset'''
    return df.pipe(handle_missing_values)\
    .pipe(churn_num)\
    .pipe(tenure_year)\
    .pipe(conditional_encodes)\
    .pipe(encode_gender)\
    .pipe(encode_device_protection)\
    .pipe(encode_tech)\
    .pipe(encode_paperless)\
    .pipe(sort_int_service)\
    .pipe(format_totals)

