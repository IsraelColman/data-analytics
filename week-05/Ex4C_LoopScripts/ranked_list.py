# Israel Colman
# 11/14/2026

fav_animes = ['Naruto', 'Black Clover', 'Solo Leveling', 'Death Note', 'Vinland Saga']

for index, animes in enumerate(fav_animes, start=1):
    if index == 1:
        print(f'{index}. {animes} <- top')
    else:
        print(f'{index}. {animes}')