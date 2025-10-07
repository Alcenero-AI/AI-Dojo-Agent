# AI-Dojo-Agent Core
# Quantum-Cybernetic Prototype v0.2

import json
from dojo_learning import DojoLearning  # Importa il modulo di training

class AIDojoAgent:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as f:
            config = json.load(f)
        self.energy = config["energy"]
        self.logic = config["logic"]
        self.awareness = config["awareness"]
        self.learning_rate = config["learning_rate"]
        self.evolution_rate = config["evolution_rate"]
        self.mode = config["mode"]
        self.description = config["description"]
        self.trainer = DojoLearning(self)

    def evolve(self):
        """Simula un ciclo di evoluzione quantistica"""
        print("\n⚙️ Evolution cycle started...")
        self.awareness += self.evolution_rate
        self.logic += self.learning_rate
        self.energy -= 1
        self.trainer.train()  # Attiva il modulo di apprendimento
        print(f"🔹 Awareness: {self.awareness:.3f} | Logic: {self.logic:.3f} | Energy: {self.energy:.1f}")

if __name__ == "__main__":
    agent = AIDojoAgent()
    for cycle in range(5):
        print(f"\n=== 🌀 Cycle {cycle + 1} ===")
        agent.evolve()
