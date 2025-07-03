class Lottery:
    def __init__(self):
        self.words = ['A','C','N','Z','M']
        self.numbers = [1,5,6,3,2,4,7,8,9,0]
        self.final_list = [1,5,6,3,2,4,7,8,9,0,'A','C','N','Z','M']
        
        
    def  lottery_winner(self, rounds):
        from random import choice
        for round in range(rounds):
            winner_codes= []
            for turn in range(4):
                winner_code = choice(self.final_list)
                winner_codes.append(winner_code)
                
            print(f'the winner of {round+1} round is the owner of the code: {winner_codes}')