import numpy as np



def data_converter(df):
    # convert time data to vector as it is better for model
    # please refer to tutorial for detail about time engineering
    # https://www.tensorflow.org/tutorials/structured_data/time_series
    date_time = df.pop('close_time')  # extract date_time as seconds
    day = 24*60*60
    year = (365.2425)*day
    df['Day sin'] = np.sin(date_time * (2 * np.pi / day))
    df['Day cos'] = np.cos(date_time * (2 * np.pi / day))
    df['Year sin'] = np.sin(date_time * (2 * np.pi / year))
    df['Year cos'] = np.cos(date_time * (2 * np.pi / year))
    df.vol = df.vol.astype(float)  # make sure vol is float
    df.close = df.close.astype(float)  # make sure close is float
    return df