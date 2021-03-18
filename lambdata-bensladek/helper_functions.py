def null_count(df):
    null = df.isnull().sum().sum()
    return print(f'Your dataset has {null} null values.')

def train_test_split(df, frac):
    shape = df.shape[0]
    train = df.iloc[:int((shape * (1 - frac)))]
    test = df.iloc[int((shape * (1 - frac))):].reset_index(drop=True)
    return train, test


def randomize(df, seed):
    randomized = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    return randomized


def rm_outlier(df):
    q1, q3 = df.quantile(0.25), df.quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - (1.5 * iqr), q3 + (1.5 * iqr)
    df = df[~((df < lower) | (df > upper)).any(axis=1)]
    return df

