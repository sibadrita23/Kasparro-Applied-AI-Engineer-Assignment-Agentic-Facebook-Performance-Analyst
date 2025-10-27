from src.orchestrator import Orchestrator
import sys

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "Analyze ROAS drop"
    Orchestrator().run(query)
