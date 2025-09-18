import numpy as np 
 
 
class Qubit:    
    def __init__(self, alpha=1 , beta=0):
        self.state = np.array([alpha,beta], dtype=complex)
        self.normalize()
        
    def normalize(self):
        norm = np.sqrt(np.abs(self.state[0])**2 + np.abs(self.state[1])**2)
        self.state = self.state / norm
        
    def set_state(self, alpha,beta):
        self.state = np.array([alpha,beta], dtype=complex)
        self.normalize()
        
    def measure_probabilities(self):
        prob_0 = np.abs(self.state[0])**2
        prob_1 = np.abs(self.state[1])**2
        return prob_0 , prob_1
    def __str__(self):
         return f"|ψ> = {self.state[0]}|0> + {self.state[1]}|1>"