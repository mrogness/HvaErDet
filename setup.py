from pathlib import Path

from setuptools import setup


README_PATH = Path(__file__).with_name("README.md")
long_description = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""


setup(
    name="hvaerdet",
    version="1.0.0",
    description="A small Norwegian-English translation Discord bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrogness/hvaerdet",
    author="Matthew Rogness",
    license="MIT",
    py_modules=["main"],
    install_requires=[
        "discord.py",
        "python-dotenv",
        "googletrans==4.0.0rc1",
    ],
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "hvaerdet=main:main",
        ],
    },
    keywords="discord bot translation norwegian english",
)