import os

from openxlab.model import download

os.system("git clone https://kkgithub.com/InternLM/InternLM.git")
os.system("mv web_demo.py ./InternLM/")

download(model_repo='YOLOv10086/internlm',
        output='./InternLM/internlm')

os.system('cd ./InternLM && streamlit run web_demo.py --server.address=0.0.0.0 --server.port 7860')

