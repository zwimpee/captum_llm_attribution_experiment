import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Parse configuration file path.")
    parser.add_argument('--config', type=str, required=True,
                        help='Path to the JSON configuration file.')
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    print("Config file path:", args.config)
