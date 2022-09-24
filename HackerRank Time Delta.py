from datetime import datetime


def delta_time(t1_str,t2_str):
    # Convert strings to datetime objects using the format specifier string
    t1 = datetime.strptime(t1_str,'%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2_str,'%a %d %b %Y %H:%M:%S %z')

    # A difference between two datetime objects is a timedelta object. Call total_seconds method
    return int((t1-t2).total_seconds())

if __name__ == '__main__':
    t1_str = 'Sun 10 May 2015 13:54:36 -0700'
    t2_str = 'Sun 10 May 2015 13:54:36 -0000'
    print(f'Time delta in seconds: {delta_time(t1_str,t2_str)}')

    t1_str = 'Sat 02 May 2015 19:54:36 +0530'
    t2_str = 'Fri 01 May 2015 13:54:36 -0000'
    print(f'Time delta in seconds: {delta_time(t1_str,t2_str)}')