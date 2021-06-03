import json
import os

if __name__ == "__main__":
    if not os.path.exists("config.json"):
        print("Please provide config.json first!")
        exit(0)

    with open("config.json") as f:
        config = json.load(f)

    os.system(f"wget ftp://cs.stanford.edu/cs/cvgl/PASCAL3D+_release1.1.zip -P {config['pascal_root']}")
    os.system(f"unzip {os.path.join(config['pascal_root'], 'PASCAL3D+_release1.1.zip')} -d {config['pascal_root']}")