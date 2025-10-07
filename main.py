# AI-Dojo-Agent Core
# Quantum-Cybernetic Prototype v0.2
import json

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

    def evolve(self):
        self.awareness += self.evolution_rate
        self.energy -= 1
        self.logic += self.learning_rate
        print(f"[{self.mode.upper()} MODE] Awareness: {self.awareness:.2f}, Logic: {self.logic:.2f}, Energy: {self.energy}")

if __name__ == "__main__":
    agent = AIDojoAgent()
    for _ in range(5):
        agent.evolve()
