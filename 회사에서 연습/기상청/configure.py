import os

base_dir = os.path.abspath(os.path.dirname(__file__))

masking_dir = os.path.join(base_dir, 'data')

# 개발환경
data_dir = os.path.join(base_dir, 'data')
# 도커 개발환경
#data_dir = "/nonsan_data/index/result/output_index"

#서버 포트 정보
serverPort = 5000

prefix = "/aci"