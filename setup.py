from setuptools import setup

setup(
    name="attendance",
    version="0.0.1",
    description="Tool to create DSCC NTU attendance messages",
    author="Ryan",
    py_modules=["attendance"],
    install_requires=["click", "jinja2"],
    entry_points={"console_scripts": ["attendance=attendance:cli"]},
)
