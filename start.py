import os

from openxlab.model import download

os.system("git clone https://kkgithub.com/InternLM/InternLM.git")
os.system("mv web_demo.py ./InternLM/")

download(model_repo='YOLOv10086/internlm', )

os.system('streamlit run InternLM/web_demo.py --server.address=0.0.0.0 --server.port 7860')

