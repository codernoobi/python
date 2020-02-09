from projectq.ops import H, Measure    #importing projectQ along with the Hadamard gate and the measuring function
from projectq import MainEngine

quantum_engine = MainEngine()       #Initialise the backend, using the emulator
qubit = quantum_engine.allocate_qubit()

H | qubit       #apply H gate to qubit which is created
Measure | qubit     #measuring the qubit after H gate
print(int(qubit))

https://dataespresso.com/en/2018/07/22/Tutorial-Generating-random-numbers-with-a-quantum-computer-Python/
https://en.wikipedia.org/wiki/Quantum_teleportation
https://en.wikipedia.org/wiki/Quantum_logic_gate
https://projectq.readthedocs.io/en/latest/projectq.setups.html?highlight=ibm