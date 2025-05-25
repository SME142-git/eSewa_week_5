import pandas as pd


class DataLoader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load_data()
        return cls._instance

    def load_data(self):
        df = pd.read_csv('final_data.csv')
        df['Date'] = pd.to_datetime(df['Date'], format='mixed')
        df.set_index('Date',inplace=True)
        self._df = df

    def get_data(self):
        return self._df
