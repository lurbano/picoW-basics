from uKnob import *

knob = uKnob(board.A1)

p = 10
print(p, knob.calcValueFromPercent(p))
print(knob.getPercent(255000), "%")

print("Knob value:", knob.getValue())
print(f"Knob percent: {knob.getPercent()}%")

