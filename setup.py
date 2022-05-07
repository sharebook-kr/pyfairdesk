"""setup
"""
import setuptools

install_requires = [
   'requests'
]

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyfairdesk',
    version='0.0.2',
    author='Jonghun Yoo, Brayden Jo',
    author_email='jonghun.yoo@pyquant.co.kr, brayden.jo@pyquant.co.kr',
    description="python wrapper for Fairdesk API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sharebook-kr/pyfairdesk',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
