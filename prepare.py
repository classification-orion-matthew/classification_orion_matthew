'''
misc functions for working with the titanic and iris dbase
'''
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

def drop_i_columns(df):
    '''drops iris columns'''
    return df.drop(columns = (['measurement_id', 'species_id']))

def rename_species(df):
    '''renames species_name to species'''
    return df.rename(index = str, columns={'species_name': 'species'})

def encode_species(df):
    '''encodes species'''
    encoder = LabelEncoder()
    encoder.fit(df.species)
    return df.assign(species_encode = encoder.transform(df.species))

def prep_iris(df):
    '''preps all of iris data'''
    return df.pipe(drop_i_columns)\
        .pipe(rename_species)\
        .pipe(encode_species)

def handle_missing_values(df):
    '''sets missing values in embarked and embark_town'''
    return df.assign(
        embark_town = df.embark_town.fillna('Other'),
        embarked = df.embarked.fillna('O')
    )

def drop_t_columns(df):
    '''drop deck'''
    return df.drop(columns = 'deck')

def encode_embarked(df):
    '''encodes embarked'''
    encoder=LabelEncoder()
    encoder.fit(df.embarked)
    return df.assign(embarked_encode = encoder.transform(df.embarked))

def prep_titanic(df):
    '''preps all of titanic'''
    return df.pipe(handle_missing_values)\
        .pipe(drop_t_columns)\
        .pipe(encode_embarked)

# binning and value_counts: 
def value_counts(dataframe):
    for col in dataframe.drop(columns=('customer_id')):
        if np.issubdtype(dataframe[col].dtype, np.number) and dataframe[col].nunique() > 10:
            print(dataframe[col].value_counts(bins=10, sort=False))
        else: 
            print(dataframe[col].value_counts(sort=False))


def handle_missing_values(dataframe):
    return dataframe.assign(
        total_charges = dataframe.total_charges.fillna(0)
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

def conditional_encodes(df):
    df['phone_id'] = np.select(conditions_lns, choices_lns)
    df['household_type_id'] = np.select(conditions_pdep, choices)
    df['streaming_services'] = np.select(conditions_strm, choices)
    df['secback'] = np.select(conditions_secback, choices)
    return df


def prep_telco_data(df):
