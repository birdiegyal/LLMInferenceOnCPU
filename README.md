These Programs will be able to run on machines with Intel Xeon Scalable Processor (SPR). if you try to run it on your machine you may get the error stating that your instruction set doesnt match with AIX which is found in Intel Xeon SPR.
# to run build_chatbot.py
```
pip install -r build_chatbot_requirements.txt
python3 build_chatbot.py
```
# to run finetuning_llama.py
```
curl -o alpaca_data.json https://raw.githubusercontent.com/tatsu-lab/stanford_alpaca/main/alpaca_data.json
pip install -r finetuning_requirements.txt
python3 finetuning_llama.py
```
