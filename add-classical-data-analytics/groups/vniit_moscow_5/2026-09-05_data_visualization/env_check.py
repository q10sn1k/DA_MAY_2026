from pathlib import Path
import sys

print("Python:", sys.version.split()[0])

required = ["pandas", "matplotlib", "seaborn"]
errors = []
for name in required:
    try:
        module = __import__(name)
        print(f"{name}: {getattr(module, '__version__', 'unknown')}")
    except Exception as exc:
        errors.append(f"{name}: {exc}")

root = Path(__file__).resolve().parent
data_file = root / "data" / "viz.csv"
print("Dataset:", data_file)
print("Dataset exists:", data_file.exists())
if not data_file.exists():
    errors.append("dataset not found: data/viz.csv")

if errors:
    print("\nERRORS:")
    for item in errors:
        print("-", item)
    raise SystemExit(1)

print("\nEnvironment check: OK")
