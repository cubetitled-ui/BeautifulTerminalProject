from setuptools import setup, find_packages

setup(
    name="beautiful-terminal",
    version="0.1.0",
    description="Красивый и функциональный терминал на Python",
    author="Titled Cube",
    author_email="titledcubeofficial@gmail.com",
    packages=find_packages(),
    install_requires=[
        "rich>=13.0.0",
        "pyfiglet>=0.8.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "beautiful-terminal=beautiful_terminal.main:main",
        ],
    },
)