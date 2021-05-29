
from setuptools import setup, find_packages


setup(
    long_description=open("README.md", "r").read(),
    name="loraspi",
    version="1.6",
    description="library for lora stuff",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/nbdy/loraspi",
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License'
    ],
    keywords="waveshare lora library",
    packages=find_packages(),
    install_requires=[
        "pyrunnable", "loguru"
    ],
    long_description_content_type="text/markdown",
)
