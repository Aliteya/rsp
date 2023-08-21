import random
from lexicon.lexicon import LEXICON_RU

def get_result() -> str:
    return random.choice(['rock', 'scissors', 'paper'])

def _norm_user_ans(user_ans: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_ans:
            break
    return key

def get_win(user_ans: str, bot_ans: str) -> str:
    user_ans = _norm_user_ans(user_ans)
    rules: dict[str, str] = {"rock" : "scissors", "scissors" : "paper", "paper" : "rock"}
    if user_ans == bot_ans:
        return "nobody nobody no body"
    elif rules[user_ans] == bot_ans:
        return "only yyyoooouuuuuuuuuu"
    else:
        return "robot"