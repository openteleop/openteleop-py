import json
from setuptools import setup, find_packages

#Debugging
import os
print("Current working directory:", os.getcwd())
print("Contents of current directory:", os.listdir())

# Load the version from version.json
# Note that version.json is added only in the context of the GH action release workflow
with open('version.json', 'r') as f:
    version_json = json.load(f)
    version = version_json['version']

setup(
    name="openteleop",
    version=version,
    packages=find_packages(),
    description="Python SDK for OpenTeleop",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/openteleop/openteleop-py",
    author="Devon Copeland",
    author_email="founders@serial.io",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    install_requires=["requests"],
    include_package_data=True
)
