# AUTOGENERATED! DO NOT EDIT! File to edit: ..\00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ..\00_card.ipynb 3
suits = ["Clubs", "Diamonds", "Hearts", "Spade"]
ranks = [None, "A"] + [str(x) for x in range(2,11)] + ["J", "Q", "K"]

# %% ..\00_card.ipynb 10
class Card:
    "A playing card, created by passing in `rank` from `ranks` and `suit` from `suits`"
    def __init__(self, suit, rank): self.suit,self.rank = suit, rank
    def __str__(self): return f"{ranks[self.rank]}{suits[self.suit]}"
    __repr__ = __str__

# %% ..\00_card.ipynb 13
@patch
def __eq__(self, a:Card): return (self.suit,self.rank)==(a.suit,a.rank)

# %% ..\00_card.ipynb 18
@patch
def __lt__(self:Card, a:Card): return (self.suit,self.rank)<(a.suit,a.rank)

# %% ..\00_card.ipynb 20
@patch
def __gt__(self:Card, a:Card): return (self.suit,self.rank)>(a.suit,a.rank)
