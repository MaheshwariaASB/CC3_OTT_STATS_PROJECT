import os

from api_handler import API_Handler
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            if os.path.exists(sys.argv[1]):
