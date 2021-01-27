# --- all relevant imports ---
import pandas as pd

# TODO possibly split date and time from datetime object.
# TODO limit duration to to decimals

def read_data():
    orig_data = pd.read_excel(r'data\KOPIE_Auswertung_Ladestationen_SmartParking.xlsx',
                              sheet_name='cpochargeevents_01.06.2019 Roh2')
    return orig_data


# --- write dataset to file ---
def write_dataset_to_file(df, filename):
    file = r'data\df_' + filename + '.csv'
    # TODO re-label columns to starttime, stoptime, duration, weekday, place, stationID
    df.to_csv(file, index=False, columns=['Start time', 'Stop time', 'Duration', 'weekday', 'station', 'Station ID'])
    print(file + " written to file")
    pass


# --- extract required columns from dataframe ---
def extract_required_data(df):
    df = df[['Station ID', 'Station name', 'Start time', 'Stop time', 'Duration']]

    # sort data along start time
    pd.to_datetime(df['Start time']).sort_values()

    # delete all entries with start time older than 01.10.2019
    from_timestamp = "2019-10-01"
    df = df[(df['Start time'] > from_timestamp)]

    # add weekday. 0=Mon, 1=Tue, ..., 6=Sun
    df['weekday'] = df['Start time'].apply(lambda x: x.weekday())

    # TODO possibly add a station identifier which is also added on parking sensors. For grouping purposes.

    # TODO simplify. Don't repeat
    # create individual dataframes for a charging station, consisting of two station id's each
    df_station_thurgauerstr = df[(df['Station ID'] == 25111) | (df['Station ID'] == 25112)]
    # TODO optimize the following assignment as stated in
    #  https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    df_station_thurgauerstr['station'] = 'Thurgauerstrasse'
    write_dataset_to_file(df_station_thurgauerstr, 'charging_thurgauerstr')

    df_station_tramstr = df[(df['Station ID'] == 24647) | (df['Station ID'] == 24648)]
    df_station_tramstr['station'] = 'Tramstrasse'
    write_dataset_to_file(df_station_tramstr, 'charging_tramstr')

    df_station_singlistr = df[(df['Station ID'] == 24649) | (df['Station ID'] == 24650)]
    df_station_singlistr['station'] = 'Singlistrasse'
    write_dataset_to_file(df_station_singlistr, 'charging_singlistr')

    pass


# --- start preparation of charging data ---
orig_charging_data = read_data()
extract_required_data(orig_charging_data)
