if __name__ == '__main__':
    'Prompt user to input hour'
    print('Type the current hour: ')
    hour = int(input())

    'Prompt user to input minutes'
    print('Type the current minutes: ')
    minutes = int(input())

    'Prompt user to input seconds'
    print('Type the current seconds: ')
    seconds = int(input())

    'Print total seconds'
    total_seconds = hour * 60 * 60 + minutes * 60 + seconds
    print(total_seconds)
