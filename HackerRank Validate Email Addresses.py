import re

def valid_email_format(address):
    """
    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores .
    The website name can only have letters and digits .
    The extension can only contain letters .
    The maximum length of the extension is 3.
    """

    rx = r'(\w|[-])+@[A-Za-z0-9]+\.[A-Za-z]{1,3}'  # According to python docs, better to use raw strings for pattern matching
    result = re.fullmatch(rx,address)

    return result

if __name__ == '__main__':
    email_address = input('Enter email address to validate: ')
    
    if valid_email_format(email_address) :
        print(f'{email_address} is valid')
    else:
        print(f'{email_address} is NOT valid')