import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="health_service",
    version="0.0.1",
    author="Anders Hofstee",
    author_email="a.hofstee@catalpainternational.org",
    description=("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license="BSD",
    keywords="example documentation tutorial",
    url="http://www.github.com/catalpainternational/health_service",
    packages=['health_service', ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
