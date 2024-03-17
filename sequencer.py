'''Sequencer attempts to solve the problem layed out in the README file'''
import argparse
import base64
import random

from Crypto.Random import get_random_bytes



def main(args):
    '''
    Main function runs through a bunch of 
    '''
    print(f'Using seed value of: {args.seed}')
    random.seed(args.seed)

    sequence = ''

    for i in range(0, 10000):
        coin_flip = random.randint(0, 1)
        if coin_flip:
            sequence += 'H'
        else:
            sequence += 'T'
    
    print(f'Final Sequence: {sequence}')
    alice_pts = 0
    bob_pts = 0
    for i in range(0, len(sequence)-1):
        test_str = sequence[i]+sequence[i+1]
        if test_str == 'HH':
            alice_pts += 1
        elif test_str == 'HT':
            bob_pts += 1
    
    print(f'Alice points: {alice_pts}')
    print(f'Bob points:{bob_pts}')

    if alice_pts == bob_pts:
        print('Perfect Draw!')
    elif (alice_pts > bob_pts):
        print('Alice Wins!')
    else:
        print('Bob Wins!')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-s', '--seed', type=str, default=base64.b64encode(get_random_bytes(16)).decode('UTF-8'), help='Input a given seed to test or verify results with.')
    args = p.parse_args()
    main(args)
