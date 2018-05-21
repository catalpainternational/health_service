import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="health_service",
    version="1.2.1",
    author="Anders Hofstee",
    author_email="a.hofstee@catalpainternational.org",
    description=("Health Service model for Catalpa's projects."),
    long_description=read('README.md'),
    license="BSD",
    url="http://www.github.com/catalpainternational/health_service",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
