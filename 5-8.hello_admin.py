usernames = ['admin', 'leo', 'manu', 'clara', 'luana']

for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Welcome back user {username.title()}')
