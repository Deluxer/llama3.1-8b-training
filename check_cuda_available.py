import torch
import os

print(torch.cuda.is_available())

print(os.getenv('HF_TOKEN'))