from dojo_learning import DojoLearning
import time

def run_quantum_cycle():
    agent = DojoLearning("config.json")

    print("🤖 Initializing AI-Dojo-Agent quantum core...")
    print(f"Mode: {agent.mode}")
    print("----------------------------------------------------")

    for cycle in range(1, 21):
        agent.train()
        status = agent.status()
        print(f"Cycle {cycle}: Energy={status['energy']:.2f}, Logic={status['logic']:.2f}, Awareness={status['awareness']:.3f}")
        time.sleep(0.5)  # Simula il tempo di elaborazione

    print("\n✅ Simulation complete. Quantum evolution stabilized.")
    print("----------------------------------------------------")
    print(agent.status())

if __name__ == "__main__":
    run_quantum_cycle()
