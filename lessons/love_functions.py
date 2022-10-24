def love(subject:str) -> str:
    """Given a subject as a parameter, returns a love string"""
    return f"I love you {subject}!"


def spread_love(to:str, n:int) -> int:
    """Generate a str repeating a loving message n times."""
    love_note: str = ""
    count: int = 0
    while count < n:
        love_note = love_note + love(to) +"\n"
        count = count + 1
    return love_note

print(love("sijin"))
print(spread_love("sijin", 3))

# to call it in the terminal
#from lessons.love_functions import spread_love

def mystery(n:int) ->str:
    """A useless function."""
    i: int = 0
    while i < n:
        if i % 2 == 1:
            return "ooh"
        i += 1
    return "ahh"
    
print(mystery(4))