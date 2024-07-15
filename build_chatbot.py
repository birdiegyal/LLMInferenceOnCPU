from intel_extension_for_transformers.neural_chat import build_chatbot, PipelineConfig
from intel_extension_for_transformers.transformers import MixedPrecisionConfig
config = PipelineConfig(optimization_config=MixedPrecisionConfig())
chatbot = build_chatbot(config)

queries = [
    "What is Summer Season?\n",
    "What is a Mango?\n",
    "Name 5 different fruits names.\n",
    "Name 2 wild animals and 3 domestic animals.\n",
    "What do you mean by Heuristics in Best-First Search Algorithm?\n"
]
index = 0
for query in queries:
    index += 1
    print(f"Q{index}.", query)
    response = chatbot.predict(query=query)
    print("response -> ", response)
