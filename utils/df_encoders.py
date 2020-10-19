import pandas as pd

# One Hot Encoding
def ohe_feature(df, feature, drop_additional_feature=True):
    encoder = pp.OneHotEncoder(categories='auto', sparse=False)
    data = encoder.fit_transform(df[feature].values.reshape(len(df[feature]), 1))
    # creating the encoded df
    ohedf = pd.DataFrame(data, columns=[feature + ': ' + str(i.strip('x0123_')) for i in encoder.get_feature_names()])
    # to drop the extra column of redundant data
    if drop_additional_feature:
        ohedf.drop(ohedf.columns[len(ohedf.columns) - 1], axis=1, inplace=True)
    # concat the ohe df with the original df
    df = pd.concat([df, ohedf], axis=1)
    # to drop the original column in the df
    del df[feature]

    return df, encoder

