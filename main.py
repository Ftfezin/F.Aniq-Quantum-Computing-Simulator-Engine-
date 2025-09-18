import numpy as np
from qubit import Qubit
from gates import X,H,Z,Y, apply_gate

q = Qubit()
print("initial qubit: ", q)
print("Probabilities:", q.measure_probabilities())

# Experiments:

# superpostion :
# apply_gate(q,H)

# Inteference (HZH):
# apply_gate(q,H)
# apply_gate(q,Z)
# apply_gate(q,H)

# double hadamard:
#apply_gate(q,X)
#apply_gate(q,X)


print(q, q.measure_probabilities())