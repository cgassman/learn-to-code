# --- all relevant imports ---
import pandas as pd

# TODO possibly split date and time after having created start and stopevents
# TODO limit duration to to decimals

# --- read in data of files ---
def read_data():
    orig_parking_data = pd.read_excel(r'data\KOPIE_Auswertung_Ladestationen_SmartParking.xlsx',
                                      sheet_name='Sensordaten Roh')
    return orig_parking_data


# --- write dataset to file ---
def write_dataset_to_file(df, filename):
    file = r'data\df_' + filename + '.csv'
    # TODO re-label columns to starttime, stoptime, duration, weekday, place, sensorID
    df.to_csv(file, index=False, columns=['starttime', 'endtime', 'duration', 'weekday', 'station', 'EUI'])
    print(file + " written to file")
    pass


# --- eliminate double entries to get a clear sequence of 0s and 1s (0,1,0,1...) of parking events
def eliminate_double_entries(df):
    # read through df and delete where double entry found:
    #  if data.parking_status == 1 (and previous is 1) delete or if data.parking_status == 0 (and previous is 0) delete
    cleared_df = pd.DataFrame()

    current = df.iloc[0, 2]
    if current == 1:
        cleared_df = cleared_df.append(df.iloc[0])  # ensure we start with a parking event for later steps
    for i in range(len(df)):
        if current != df.iloc[i, 2]:
            cleared_df = cleared_df.append(df.iloc[i])
            current = df.iloc[i, 2]

    return cleared_df


# --- create start/stop timestamps ---
def create_start_stop_events(df):
    # create new dataframe with EUI, starttime, endtime
    new_df = pd.DataFrame(columns=["EUI", "starttime", "endtime", "duration"])

    i = 0
    while i < (len(df) - 1):
        eui = df.iloc[i, 0]
        starttime = df.iloc[i, 5]
        endtime = df.iloc[i+1, 5]
        duration = ((endtime - starttime).total_seconds())/60  # TODO use timedelta instead?
        new_df = new_df.append({"EUI": eui,
                                "starttime": starttime,
                                "endtime": endtime,
                                "duration": duration}, ignore_index=True)
        i += 2

    return new_df


# --- work on park_sensor data ---
def clean_up_parking_data(df, timestamp):

    # TODO can this be achieved without timestamp as parameter but with direct access?
    # TODO is to_datetime required or can sort_values(by='timestamp') be used?
    # sort data along timestamp
    pd.to_datetime(df[timestamp]).sort_values()

    # delete all entries older than 01.10.2019
    from_timestamp = "2019-10-01"
    df = df[(df[timestamp] > from_timestamp)]

    # TODO beautify this code. Don't repeat.
    # split park_sensor data by EUI
    df_sensor_193996 = df.loc[(df['EUI'] == 'FCD6BD0000193996')]
    df_sensor_193999 = df.loc[(df['EUI'] == 'FCD6BD0000193999')]
    df_sensor_19396E = df.loc[(df['EUI'] == 'FCD6BD000019396E')]
    df_sensor_193976 = df.loc[(df['EUI'] == 'FCD6BD0000193976')]
    df_sensor_193977 = df.loc[(df['EUI'] == 'FCD6BD0000193977')]
    df_sensor_193982 = df.loc[(df['EUI'] == 'FCD6BD0000193982')]

    # eliminate double entries of 0s and 1s to get a clear 0, 1, 0, 1... file of parking events
    cleaned_parking_sensor_193996 = eliminate_double_entries(df_sensor_193996)
    cleaned_parking_sensor_193999 = eliminate_double_entries(df_sensor_193999)
    cleaned_parking_sensor_19396E = eliminate_double_entries(df_sensor_19396E)
    cleaned_parking_sensor_193976 = eliminate_double_entries(df_sensor_193976)
    cleaned_parking_sensor_193977 = eliminate_double_entries(df_sensor_193977)
    cleaned_parking_sensor_193982 = eliminate_double_entries(df_sensor_193982)

    parking_events_193996 = create_start_stop_events(cleaned_parking_sensor_193996)
    parking_events_193999 = create_start_stop_events(cleaned_parking_sensor_193999)
    parking_events_19396E = create_start_stop_events(cleaned_parking_sensor_19396E)
    parking_events_193976 = create_start_stop_events(cleaned_parking_sensor_193976)
    parking_events_193977 = create_start_stop_events(cleaned_parking_sensor_193977)
    parking_events_193982 = create_start_stop_events(cleaned_parking_sensor_193982)

    # TODO combine sensors to one station?
    parking_events_thurgauerstr = parking_events_193996.append(parking_events_193999).sort_values(by='starttime')
    parking_events_singlistr = parking_events_193982.append(parking_events_193977).sort_values(by='starttime')
    parking_events_tramstr = parking_events_193976.append(parking_events_19396E).sort_values(by='starttime')

    # TODO add weekday for starttime
    parking_events_thurgauerstr['weekday'] = parking_events_thurgauerstr['starttime'].apply(lambda x: x.weekday())
    parking_events_singlistr['weekday'] = parking_events_singlistr['starttime'].apply(lambda x: x.weekday())
    parking_events_tramstr['weekday'] = parking_events_tramstr['starttime'].apply(lambda x: x.weekday())

    # TODO add station group identifier for grouping purposes. The same identifier should be added in charging data
    parking_events_thurgauerstr['station'] = 'Thurgauerstrasse'
    parking_events_tramstr['station'] = 'Tramstrasse'
    parking_events_singlistr['station'] = 'Singlistrasse'

    # write parking events to file
    write_dataset_to_file(parking_events_thurgauerstr, 'parking_thurgauerstr')
    write_dataset_to_file(parking_events_tramstr, 'parking_tramstr')
    write_dataset_to_file(parking_events_singlistr, 'parking_singlistr')

    pass


# --- start data preparation for parking data ---
orig_data = read_data()
clean_up_parking_data(orig_data, 'timestamp')
