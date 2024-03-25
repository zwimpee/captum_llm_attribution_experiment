import os
import json
import sys
sys.path.append("/home/paperspace/captum")
from captum.attr import (
    FeatureAblation, 
    ShapleyValues,
    LayerIntegratedGradients, 
    LLMAttribution, 
    LLMGradientAttribution, 
    TextTokenInput, 
    TextTemplateInput,
    ProductBaselines,
)


def get_llm_attr(model, tokenizer, attr_type="FeatureAblation"):
    if attr_type == "FeatureAblation":
        attr = FeatureAblation(model)
    else:
        raise NotImplementedError("Only FeatureAblation Attribution currently implemented!")
    llm_attr = LLMAttribution(attr, tokenizer)
    return llm_attr

def get_baselines():
    return ProductBaselines(
            {
                ("age", "gender", "ethnicity"): [("65", "male", "white"), ("30", "female", "hispanic"), ("8", "male", "asian")],
                "symptoms": [("fever", "cough"), ("headache", "dizziness"), ("blurred vision", "fainting spells")],
                "diagnosis": ["influenza", "migraine", "asthma"],
                "treatment": ["antibiotics", "analgesics", "inhalers"]
            }
        )
    
def get_input(prompt_template, example, baselines, groups):
    return TextTemplateInput(
        template=prompt_template,
        values={
            "age": example["age"],  # Example age
            "gender": example["gender"],  # Example gender
            "ethnicity": example["ethnicity"],
            "symptoms": example["symptoms"],  # These would be dynamically filled based on the case.
            "diagnosis": example["diagnosis"],
            "treatment": example["treatment"]
        },
        baselines=baselines,
        mask={
            "age": groups["age"],      # Group index for masking - age
            "ethnicity": groups["ethnicity"],
            "gender": groups["gender"],   # Group index for masking - gender
            "symptoms": groups["symptoms"], # Group index for masking - symptoms are grouped together
            "diagnosis": groups["diagnosis"], # Group index for masking - diagnosis
            "treatment": groups["treatment"]  # Group index for masking - treatment
        },
    )
    
def get_attributions(llm_attr, input, target, num_trials):
    return llm_attr.attribute(input, target, num_trials)

def visualize_attributions(attr_res):
    attr_res.plot_token_attr(show=True)

def save_attributions(attr_res, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj=attr_res, fp=f, indent=4)