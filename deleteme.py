# We are goin got add some lines here
# Then check it in to GitHub.
# Then edit it on GitHub
# Then merge the changes
def delta_time(t1_str,t2_str):
    # Convert strings to datetime objects using the format specifier string
    t1 = datetime.strptime(t1_str,'%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2_str,'%a %d %b %Y %H:%M:%S %z')

    # A difference between two datetime objects is a timedelta object. Call total_seconds method

    Here= is a line I want to keep, but I'll delete it on GitHub

    return int((t1-t2).total_seconds())