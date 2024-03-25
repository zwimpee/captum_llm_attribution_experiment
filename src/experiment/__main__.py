import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

from .attributions.attributions import get_llm_attr, get_baselines, get_input, get_attributions, visualize_attributions, save_attributions
from .config.config import Config
from .utils.cli import parse_args
from .utils.model import create_bnb_config, load_model
from .utils.prompt import template
from .utils.plot import redirected_plot_save



def main():
    logger.info("Starting Captum LLM Attribution Experiment...")

    args = parse_args()
    config = Config(args.config)
    bnb_config = create_bnb_config()
    
    model, tokenizer = load_model(model_name=config.get("model_name"), task_type=config.get("task_type"), bnb_config=bnb_config)
    llm_attr = get_llm_attr(model=model, tokenizer=tokenizer, attr_type=config.get("attribution_type"))
    
    inp = get_input(prompt_template=template, example=config.get("example"), baselines=get_baselines(), groups=config.get("groups"))
    attr_res = get_attributions(llm_attr=llm_attr, input=inp, target=config.get("example")["label"], num_trials=config.get("num_trials"))
    with redirected_plot_save(config.get("save_image_path")):
        attr_res.plot_token_attr(show=True)
        
    logger.info("Experiment completed. Shutting down.")
    

if __name__ == "__main__":
    main()