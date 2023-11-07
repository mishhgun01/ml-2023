def country_to_number(df):
    if df['COUNTRY'] == 'Turkey':
        val = 0
    elif df['COUNTRY'] == 'Ukraine':
        val = 1
    else:
        val = 2
    return val

def admin_to_number(df):
    if df['ADMIN1'] == 'Donetsk':
        val = 0
    elif df['ADMIN1'] == 'Luhansk':
        val = 1
    else:
        val = 2
    return val