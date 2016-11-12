from os.path import dirname, abspath


# Here we do the IO readings, whatever that is. Right now is just reading a csv file.
def read_transactions():
    # Replace with whatever is necessary
    p = dirname(dirname(abspath(__file__)))
    with open('%s/static/data/mock_transaction_data.json' % p, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        return data
    return None


def extract_dataframe(json):
    pass


def get_historic_stats(data, date_point):
    pass


def get_last_cash_injection(data):
    pass


def make_suggestions(pk_user):
    return read_transactions()
