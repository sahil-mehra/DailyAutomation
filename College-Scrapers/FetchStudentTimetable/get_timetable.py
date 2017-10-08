import sys
import webbrowser


def get_url(default):
    while True:
    
        semester1 = 'week1=1&week2=12'
        semester2 = 'week1=20&week2=31'

        program=''
        year=''

        program = str(input('Please enter your program code: ')).upper()
        year = str(input('Please enter your year number: '))
        semester = str(input('Please enter your semester number, 1 or 2: '))
    
        if semester == '1':
            semester = semester1
            break
        elif semester == '2':
            semester = semester2
            break
        else:
            break

    if default[0] == '' or default[1] == '' or default[2] == '':
        return 'Not a valid input.'

    url = default[0] + program + default[1] + year + default[2] + semester + default[3]
    return url
    

def get_url_from_args(details, default):

    semester1 = 'week1=1&week2=12'
    semester2 = 'week1=20&week2=31'

    program=''
    year=''

    if len(details) == 0:
        url = get_url()
        webbrowser.open(url)
        sys.exit()

    elif len(details) < 3 and len(details) >= 0:
        print("Not a valid input.")
        sys.exit()

    elif len(details) > 3:
        print("Not a valid input.")
        sys.exit()

    else:
        program = sys.argv[1]
        year = sys.argv[2]
        semester = sys.argv[3]

        if semester == '1':
            semester = semester1

        elif semester == '2':
            semester = semester2

        else:
            print("Not a valid input.")
            sys.exit()

    url = default[0] + program + default[1] + year + default[2] + semester + default[3]
    return url


def main():

    default = 'https://www101.dcu.ie/timetables/feed.php?prog=_&per=_&_&hour=1-28&template=student'
    default = default.split('_')
    

    details = sys.argv[1:]

    if len(details) == 0:
        url = get_url(default)
        webbrowser.open(url)
        sys.exit()

    elif len(details) < 3 and len(details) >= 0:
        print("Not a valid input.")
        sys.exit()

    else:
        url = get_url_from_args(details, default)
        webbrowser.open(url)
        sys.exit()

if __name__ == '__main__':
main()
