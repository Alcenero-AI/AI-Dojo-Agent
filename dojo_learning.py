import json
import random

class DojoLearning:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.energy = self.config["energy"]
        self.logic = self.config["logic"]
        self.awareness = self.config["awareness"]
        self.learning_rate = self.config["learning_rate"]
        self.evolution_rate = self.config["evolution_rate"]
        self.mode = self.config["mode"]

    def train(self):
        # Simula un ciclo di apprendimento quantistico-cibernetico
        delta = random.uniform(-1, 1) * self.learning_rate
        self.awareness = max(0, self.awareness + delta)
        self.energy = max(0, self.energy - abs(delta) * 10)
        self.logic = min(200, self.logic + abs(delta) * 5)
        self.adapt()

    def adapt(self):
        # Evoluzione dinamica basata sulla modalità
        if self.mode == "adaptive":
            self.learning_rate *= (1 + random.uniform(-0.05, 0.05))
            self.evolution_rate *= (1 + random.uniform(-0.02, 0.02))

    def status(self):
        return {
            "energy": self.energy,
            "logic": self.logic,
            "awareness": self.awareness,
            "learning_rate": self.learning_rate,
            "evolution_rate": self.evolution_rate
        }

if __name__ == "__main__":
    agent = DojoLearning()
    for _ in range(10):
        agent.train()
        print(agent.status())
