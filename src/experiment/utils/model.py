import torch 
from transformers import AutoModelForCausalLM, AutoModelForSequenceClassification, BitsAndBytesConfig, AutoTokenizer

def load_model(model_name, task_type, bnb_config):
    n_gpus = torch.cuda.device_count()
    max_memory = "10000MB"

    if task_type == "CausalLM":
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            quantization_config=bnb_config,
            device_map="auto", # dispatch efficiently the model on the available ressources
            max_memory = {i: max_memory for i in range(n_gpus)},
        )
    elif task_type == "SequenceClassification":
        num_labels = 2
        id2label = {0: "today/tomorrow", 1: "longer"}
        label2id = {v: k for k,v in id2label.items()}
        model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            quantization_config=bnb_config,
            num_labels=num_labels,
            id2label=id2label,
            label2id=label2id,
            device_map="auto", # dispatch efficiently the model on the available ressources
            max_memory = {i: max_memory for i in range(n_gpus)},
        )
        
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=True)

    # Needed for LLaMA tokenizer
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.pad_token_id = tokenizer.eos_token_id

    return model, tokenizer

def create_bnb_config():
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    return bnb_config