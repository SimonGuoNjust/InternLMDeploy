import os

from openxlab.model import download

# download(model_repo='YOLOv10086/internlm',
#         output='./adapter')

os.system('streamlit run web_demo.py --server.address=0.0.0.0 --server.port 7860')

