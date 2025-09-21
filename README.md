# aniQ Quantum Computing Simulator Engine

* **aniQ Quantum Computing Simulator Engine** is a Python library that simulates quantum computing concepts, qubits, and quantum states. It offers a simple, educational, and user-friendly environment for students, enthusiasts, and developers new to quantum computing, to investigate quantum mechanics and quantum information concepts. 

For now its 1 qubit system , 
* **Single Qubit Representation** - Define and manipulate qubits with user-defined quantum states.

* **State Normalization** - Guarantees that any qubit state maintains valid quantum probabilities. 

* **Readable Output** - Outputs the qubit state in Dirac notation (|ψ> = α|0> + β|1>).

* **Lightweight & Educational** - Geared towards understanding quantum state representation and basic quantum operations.
I built everything from scratch , pure maths into coding

# Installation

```bash
git clone https://github.com/Ftfezin/aniQ-QSim.git
pip install numpy
```

# Usage example 
```python
q = Qubit()
print(q)
apply_gate(q,H) # qubit & gate
print(q)
plot_bloch_sphere(q,title="after gate")
q.measure()
```