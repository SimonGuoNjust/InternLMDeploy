import os

from openxlab.model import download

os.system("git clone https://kkgithub.com/InternLM/InternLM.git")
os.system("mv web_demo.py ./InternLM/")

download(model_repo='YOLOv10086/internlm', 
         output="./internlm",
         model_name=['tokenizer.model', 'upload.py', 'config.json', 'pytorch_model.bin.index.json', 'configuration_internlm.py', 'pytorch_model-00003-of-00008.bin', '.ipynb_checkpoints', 'pytorch_model-00004-of-00008.bin', 'tokenizer_config.json', 'pytorch_model-00008-of-00008.bin', 'pytorch_model-00007-of-00008.bin', 'special_tokens_map.json', 'added_tokens.json', 'pytorch_model-00006-of-00008.bin', 'pytorch_model-00002-of-00008.bin', 'modeling_internlm.py', 'pytorch_model-00001-of-00008.bin', 'tokenization_internlm.py', 'pytorch_model-00005-of-00008.bin', 'generation_config.json'])

os.system('streamlit run InternLM/web_demo.py --server.address=0.0.0.0 --server.port 7860')

