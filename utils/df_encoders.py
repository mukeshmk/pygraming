import pandas as pd
from sklearn import preprocessing as pp

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

# Label Encoding
def label_encode_feature(df, feature):
    encoder = pp.LabelEncoder()
    data = encoder.fit_transform(df[feature].values.reshape(len(df[feature]), 1))
    # to drop the original column in the df
    del df[feature]
    # creating the encoded df
    ledf = pd.DataFrame(data, columns=[feature])
    # concat the ohe df with the original df
    df = pd.concat([df, ledf], axis=1)

    return df, encoder

# encoding the dataset using target encoding
def target_encode(train_df, target_variable, cat_cols, alpha):
    te_train = train_df.copy()
    globalmean = train_df[target_variable].mean()
    cat_map = dict()
    def_map = dict()

    for col in cat_cols:
        cat_count = train_df.groupby(col).size()
        target_cat_mean = train_df.groupby(col)[target_variable].mean()
        reg_smooth_val = ((target_cat_mean * cat_count) + (globalmean * alpha)) / (cat_count + alpha)

        te_train.loc[:, col] = te_train[col].map(reg_smooth_val)
        te_train[col].fillna(globalmean, inplace=True)

        cat_map[col] = reg_smooth_val
        def_map[col] = globalmean
    return te_train, cat_map, def_map
