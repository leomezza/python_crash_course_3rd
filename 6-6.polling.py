favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

poll = ['leo', 'cla', 'sarah', 'phil']

for name in poll:
    if name in favorite_languages:
        print(f'Thanks for responding to the poll, {name.title()}!')
    else:
        print(f'Please take the poll, {name.title()}.')
