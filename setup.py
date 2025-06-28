from setuptools import setup, find_packages

setup(
    name="suttonbarto",
    version="0.1.0",
    description="Reinforcement Learning Exercises from Sutton & Barto",
    author="David Bellamy",
    packages=find_packages(),
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)