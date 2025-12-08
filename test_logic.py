from logic.facts import Fact
from logic.rules import Rule
from logic.knowledge import KnowledgeBase
from logic.inference_engine import InferenceEngine

kb = KnowledgeBase()

# Add some rules
kb.add_rule(Rule(["fever", "cough"], "flu"))
kb.add_rule(Rule(["flu"], "stay_home"))

# Add initial facts (simulating user input)
kb.add_fact(Fact("fever", True))
kb.add_fact(Fact("cough", True))

engine = InferenceEngine(kb)
print(engine.forward_chain())

# See all facts
print(kb.facts)

