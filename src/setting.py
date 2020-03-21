import os
import sys

ROOT_PATH = os.path.split(os.path.abspath(__file__))[0]

environ_dict = os.environ

sys.path.append(ROOT_PATH)

HOST = environ_dict.get('BLOG_HOST', '0.0.0.0')
PORT = environ_dict.get('BLOG_PORT', '8090')
