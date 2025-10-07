# dojo_learning.py
# Quantum-Learning Core for AI-Dojo-Agent v0.3

import random
import math

class DojoLearning:
    def __init__(self, agent):
        self.agent = agent

    def train(self):
        """Adaptive quantum training loop"""
        harmony = (self.agent.logic * 0.4 + self.agent.awareness * 0.6)
        quantum_noise = random.uniform(-0.03, 0.03)

        # Adjust learning rate dynamically
        adjustment = (1 + quantum_noise) * (harmony / 100)
        self.agent.logic += adjustment
        self.agent.awareness += adjustment * 0.5
        self.agent.energy -= abs(quantum_noise * 10)

        # Keep values in range
        self.agent.energy = max(0, min(self.agent.energy, 100))
        self.agent.logic = round(self.agent.logic, 3)
        self.agent.awareness = round(self.agent.awareness, 3)

        print(f"🧠 Quantum training | Logic: {self.agent.logic} | Awareness: {self.agent.awareness} | Energy: {self.agent.energy}")
