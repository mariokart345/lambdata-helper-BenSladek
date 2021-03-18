class Helper:
    def __init__(self, data):
        self.data = data

    # Displays null count of dataframe
    def null_count(self):
        null = self.isnull().sum().sum()
        return "Your dataset contains {} null values".format(null)

    # Randomizes order of dataframe and resets index
    def randomize(self, seed):
        randomized = self.sample(frac=1, random_state=seed).reset_index(drop=True)
        return randomized

    # Takes shape and splits on fractional value given - returns 2 dataframes
    def train_test_split(self, frac):
        shape = self.shape[0]
        train = self.iloc[: int((shape * (1 - frac)))]
        test = self.iloc[int((shape * (1 - frac))):].reset_index(drop=True)
        return train, test

    # Using only pandas methods, removes outliers via interquartile ranges
    def rm_outlier(self):
        q1 = self.quantile(0.25)
        q3 = self.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - (1.5 * iqr)
        upper = q3 + (1.5 * iqr)
        df = self[~((self < lower) | (self > upper)).any(axis=1)]
        return df

