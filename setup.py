from setuptools import setup

setup(
    name="wooting-rgb",
    version="0.0.1",
    author="Alcasa",
    author_email="alcasa@arsbrevis.de",
    packages=["wooting_rgb"],
    scripts=["bin/wooting_rgb_reset.py"],
    license="LICENSE.txt",
    description="Python bindings for Wooting RGB SDK",
)
