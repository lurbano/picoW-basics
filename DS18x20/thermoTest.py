from DS18x20.uDS18x20 import *

thermo = uDS18X20(board.GP5)

T = thermo.read()

print(f"Temperature = {T}")
