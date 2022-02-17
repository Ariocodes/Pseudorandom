"""
Author: github.com/Ariocodes
This is a mini code showing how Pseudorandom generates random numbers.
"""

def pseudorandom():
    """
    Generates a random number from 0 to 10 using the Pseudo algorithm
    """
    from datetime import datetime
    now = datetime.now()
    now_in_ms = now.hour*3600000 + now.minute*60000 + now.second*1000 + round(now.microsecond/1000)
    seed = now_in_ms % 11
    result = seed * 8 % 11
    return result

print(pseudorandom())
