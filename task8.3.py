class NotNumError(Exception):
    def __init__(self, txt):
        self.txt = txt


complete = []
while True:
    try:
        enter = input('Enter a digit: ')
        if enter.isdigit():
            complete.append(int(enter))
        else:
            raise NotNumError('This is not a number')
    except NotNumError as n:
        print(n)
        question = input('Enter STOP to exit: ')
        if question.lower() == 'stop':
            print(f'This is your list of numbers: {complete}')
            break
        else:
            continue
