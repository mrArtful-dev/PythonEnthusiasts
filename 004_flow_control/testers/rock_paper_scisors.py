import random
variants = ['Rock', 'Paper', 'Scissors']
results = {'Player1': 0, 'Player2': 0}

for num in range(0, 1000000):
    player1 = variants[random.randint(0, 2)]
    player2 = variants[random.randint(0, 2)]
    if player1 == 'Rock':
        if player2 == 'Paper':
            print(f'{player1} - WIN -> {player2}')
            results['Player2'] += 1
        elif player2 == 'Scissors':
            print(f'{player1} <- WIN - {player2}')
            results['Player1'] += 1
        elif player2 == 'Rock':
            print(f'{player1} - DRAW - {player2}')
    elif player1 == 'Paper':
        if player2 == 'Paper':
            print(f'{player1} - DRAW - {player2}')
        elif player2 == 'Scissors':
            print(f'{player1} - WIN -> {player2}')
            results['Player2'] += 1
        elif player2 == 'Rock':
            print(f'{player1} <- WIN - {player2}')
            results['Player1'] += 1
    elif player1 == 'Scissors':
        if player2 == 'Paper':
            print(f'{player1} <- WIN - {player2}')
            results['Player1'] += 1
        elif player2 == 'Scissors':
            print(f'{player1} - DRAW - {player2}')
        elif player2 == 'Rock':
            print(f'{player1} - WIN -> {player2}')
            results['Player2'] += 1


print(f'Player 1 won {results["Player1"]}')
print(f'Player 2 win {results["Player2"]}')
