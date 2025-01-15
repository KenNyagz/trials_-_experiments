#! /usr/bin/env python3 
# -*- coding: utf-8 -*- 
# Fart Space Programmer


from decimal import Decimal # importing decimal to do divisions in base 10 and avoid issues that occur due to binary division


def arbitrageCalc(win_const: float, draw: float, away_win: float):
    probability = Decimal((1 / win_const)) + Decimal(1 / draw) + Decimal(1 / away_win) # If probability < 1 then profitable, if >1 loss-making, if 0 break-even
    amount = 10_000 # Sample amount to stake
    home_win_stake = (Decimal((1 / win_const)) / probability) * amount # For visualisation and calculation sake
    draw_stake = (Decimal(1 / draw) / probability) * amount # For visualisation and calculation sake
    away_win_stake = (Decimal(1 / away_win) / probability) *amount # For visualisation and calculation sake
    return probability, home_win_stake, draw_stake, away_win_stake # probaility is the only value that matters, the rest are for some explanation Nick was expalining

def main():
    result: float = arbitrageCalc(1.87,4.03, 3.79) # Sample odds as args
    print(result) #Viz

if __name__ == "__main__":
    main()
