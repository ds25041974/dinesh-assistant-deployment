"""Setup script for the Github Projectr package."""

from setuptools import find_packages, setup

setup(
    name="github-projectr",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "jinja2",
        "python-multipart",
        "aiofiles",
    ],
    python_requires=">=3.8",
)
