import pandas as pd
from os.path import dirname, abspath

# Example transaction
# [{"pk_user":1,"trn_id":"7ec1b42d-9ea4-4c40-b762-29c31f3588f0","trn_time":"2/15/2016","trn_amt":6.12}

# Change column names here to adjust to the json structure.


TRN_USER_COL = 'pk_user'
TRN_DATE_COL = 'trn_time'
TRN_AMT_COL = 'trn_amt'
TRN_HISTORY_INITIAL_WEEKS = 1
TRN_HISTORY_WEEKS_SPAN = 26
C = 35 / 100


# Here we do the IO readings, whatever that is. Right now is just reading a csv file.
def read_transactions():
    # Replace with whatever is necessary
    p = dirname(dirname(abspath(__file__)))
    with open('%s/static/data/mock_transaction_data.json' % p, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        return data
    return None


def extract_dataframe(json):
    return pd.read_json(json)


def get_saving_recc(data, pk_user, last_saving_date=None):
    # first filter by user - this shouldn't be necessary, but just in case
    user_data = data[data[TRN_USER_COL] == pk_user].sort_values(TRN_DATE_COL, ascending=False)

    # Get the first week worth of time

    initial_threshold = user_data[TRN_DATE_COL].iloc[0] - pd.Timedelta(weeks=TRN_HISTORY_INITIAL_WEEKS)

    # timestamps grow as dates are nearer

    initial_week = user_data[user_data[TRN_DATE_COL] >= initial_threshold]

    # Get the remaining weeks worth of time, in this case doing only 26

    last_threshold = user_data[TRN_DATE_COL].iloc[0] - pd.Timedelta(weeks=TRN_HISTORY_WEEKS_SPAN)

    remaining_weeks = user_data[
        (user_data[TRN_DATE_COL] < initial_threshold) & (user_data[TRN_DATE_COL] >= last_threshold)]

    print(len(initial_week))
    print(len(remaining_weeks))

    last_earning = initial_week[initial_week[TRN_AMT_COL] > 0].head(n=1)[TRN_AMT_COL].iloc[0]

    # Here is where we do the logic for the whole "no income this week" scenario
    if last_earning <= 0:
        pass

    # Get only the interesting columns from the last weeks
    remaining_weeks = remaining_weeks[remaining_weeks[TRN_AMT_COL] > 0][TRN_AMT_COL]
    mean = remaining_weeks.mean()
    std = remaining_weeks.std()

    norm = last_earning - mean + std

    return (C * (norm / std) * norm) / 2


def make_suggestions(pk_user):
    json = read_transactions()
    data = extract_dataframe(json)
    return get_saving_recc(data, pk_user)

if __name__ == '__main__':
    print("Suggestion: "+str(make_suggestions(1)))