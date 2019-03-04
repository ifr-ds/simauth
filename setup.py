from setuptools import find_packages, setup

requirements = """
pytest
flake8
falcon>=1.4,<2
gunicorn
"""


setup(
    name='simauth',
    packages=find_packages(),
    install_requires=requirements,
    version='0.1.0',
    description='Simple authorization microservice',
    author='IFResearch DataScience',
    license='MIT'
)
