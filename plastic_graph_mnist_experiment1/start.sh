python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python run_mnist_experiment.py \
  --epochs 3 \
  --hidden-units 4096 \
  --active-hidden 128 \
  --max-train 10000 \
  --max-test 2000