# Training Llama-3.1-8B

## Run main.py to train the model
## Save the model Meta-Llama-3.1-8B-bnb-4bit in Huggingface
```shell
python main.py
```

## Convert the model to GGUF format
```shell
python convert_hf_to_gguf.py
```

## Create ollama model
```shell
ollama create -f Modelfile geradeluxer/llama3.1-q4-python
```


HiggingFace model [Meta-Llama-3.1-8B-bnb-4bit](https://huggingface.co/geradeluxer/Meta-Llama-3.1-8B-bnb-4bit)
```
geradeluxer/Meta-Llama-3.1-8B-bnb-4bit
```


Ollama model [llama3.1-q4-python](https://ollama.com/geradeluxer/llama3.1-q4-python)
```
ollama run geradeluxer/llama3.1-q4-python
```

