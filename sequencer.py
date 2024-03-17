'''Sequencer attempts to solve the problem layed out in the README file'''
import argparse
import base64
import random
from tqdm import tqdm

from Crypto.Random import get_random_bytes

def run_sequence(seed, rounds: int):
    random.seed(seed)

    sequence = ''
    for i in range(0, rounds):
        coin_flip = random.randint(0, 1)
        if coin_flip:
            sequence += 'H'
        else:
            sequence += 'T'
    
    alice_pts = 0
    bob_pts = 0
    for i in range(0, len(sequence)-1):
        test_str = sequence[i]+sequence[i+1]
        if test_str == 'HH':
            alice_pts += 1
        elif test_str == 'HT':
            bob_pts += 1
    
    winner = ''
    if alice_pts == bob_pts:
        winner = 'draw'
    elif (alice_pts > bob_pts):
        winner = 'alice'
    else:
        winner = 'bob'

    return {'seed':seed, 'sequence':sequence, 'alice_pts':alice_pts, 'bob_pts':bob_pts, 'winner':winner}

def beeg_analyzer(sequences: list):
    average_alice_pts = 0
    average_bob_pts = 0
    rounds = 0

    alice_wins = 0
    bob_wins = 0

    print('Processing results in the Beeg Analyzer')
    for i in tqdm(sequences):
        alice_pts = i['alice_pts']
        bob_pts = i['bob_pts']
        winner = i['winner']
        rounds += 1
        average_alice_pts += alice_pts
        average_bob_pts += bob_pts

        if winner == 'alice':
            alice_wins += 1
        else:
            bob_wins += 1
    
    average_alice_pts = average_alice_pts/rounds
    average_bob_pts = average_bob_pts/rounds

    general_winner = ''
    if alice_wins == bob_wins:
        general_winner = 'draw'
    elif alice_wins > bob_wins:
        general_winner = 'alice'
    else:
        general_winner = 'bob'

    return (average_alice_pts, average_bob_pts, general_winner)

def gen_seeds(init_seed, rounds):
    seeds = []
    random.seed(init_seed)
    seeds.append(init_seed)
    print('Generating Seeds')
    for i in tqdm(range(0, rounds)):
        new_seed = base64.b64encode(random.randbytes(16)).decode('UTF-8')
        random.seed(new_seed)
        seeds.append(new_seed)
    return seeds    

def main(args):
    '''
    Main function runs through a bunch of 
    '''
    print(f'Using initial seed value of: {args.seed}')

    sequences = []
    seeds = gen_seeds(args.seed, args.rounds)

    print('Flipping coins...')
    for i in tqdm(range(0, args.rounds)):
        sequences.append(run_sequence(seeds[i], args.rounds))

    average_alice, average_bob, winner = beeg_analyzer(sequences)
    
    print(f'Alice had an average score of: {average_alice}')
    print(f'Bob had an average score of: {average_bob}')
    print(f'The overall winner though is: {winner}')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-s', '--seed', type=str, default=base64.b64encode(get_random_bytes(16)).decode('UTF-8'), help='Input a given seed to test or verify results with.')
    p.add_argument('-r', '--rounds', type=int, default=100, help='Change the number of rounds being used per sequence')
    args = p.parse_args()
    main(args)
