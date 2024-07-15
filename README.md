#PS4: Introduction to GenAI and Simple LLM Inference on CPU and finetuning of LLM Model to create a Custom Chatbot

These Programs will be able to run on machines with Intel Xeon Scalable Processor (SPR). if you try to run it on your machine you may get the error stating that your instruction set doesnt match with AIX which is found in Intel Xeon SPR.
# To run build_chatbot.py
```
pip install -r build_chatbot_requirements.txt
python3 build_chatbot.py
```
# To run finetuning_llama.py
```
curl -o alpaca_data.json https://raw.githubusercontent.com/tatsu-lab/stanford_alpaca/main/alpaca_data.json
pip install -r finetuning_requirements.txt
python3 finetuning_llama.py
```
# Project Report
### Note: finetuning is done only for text-generation problem using alpaca dataset.
[click here to view report](https://github.com/birdiegyal/LLMInferenceOnCPU/blob/master/LLMInferenceOnXeonSPR.pdf)
