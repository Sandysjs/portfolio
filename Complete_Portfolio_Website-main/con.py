from lottie.utils import extract
from lottie.importers import from_lottie_file
import json

# Load and extract the .lottie file
lottie_path = "/mnt/data/Animation - 1744217627327 (1).lottie"
animation = from_lottie_file(lottie_path)

# Extract the first animation from the .lottie file
json_data = animation.to_dict()

# Save as .json
json_path = "/mnt/data/animation_converted.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

json_path
