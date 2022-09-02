from setuptools import setup, find_packages

setup(
    name="package",  ##注意和文件夹名一致
    version="0.0.1",
    description=(
        "package，test packaging xxx"
    ),
    # long_description=open("README.rst").read(),
    author="zfree",
    author_email="410254835@qq.com",
    maintainer="zfree",
    maintainer_email="410254835@qq.com",
    packages=find_packages(),
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)