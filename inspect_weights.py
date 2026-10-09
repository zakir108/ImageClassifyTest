from pathlib import Path
from safetensors.numpy import load_file

path = Path(__file__).with_name("mpox.safetensors")
weights = load_file(str(path))
for name, tensor in sorted(weights.items()):
    print(f"{name}: shape={tensor.shape}, dtype={tensor.dtype}")
