from setuptools import setup, find_packages

setup(
    name="FusionThreatNet",
    version="1.0.0",
    author="Manoj Kumar Sunkara",
    description="Attention-Enhanced Transformer-VAE Framework for Cyber Attack Detection and Risk Assessment",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "scipy",
        "torch",
        "tensorflow",
        "matplotlib",
        "seaborn",
        "tqdm",
        "joblib"
    ],
    python_requires=">=3.10",
)