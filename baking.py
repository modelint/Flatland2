"""
baking.py – Not part of flatland.  Just here to test something
"""

from morning_bun import MorningBun

print(f"Not ready: Temp={MorningBun.temp}, Flavor={MorningBun.flavor}")
MorningBun()
print(f"Ready now: Temp={MorningBun.temp}, Flavor={MorningBun.flavor}")
