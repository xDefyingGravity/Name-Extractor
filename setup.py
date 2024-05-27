from setuptools import setup, find_packages

setup(
    name='NameExtractor',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    author="Defying Gravity",
    description="Name Extractor is a small AI program to extract name and gender from characters in text."
    
)
