import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="s2rcp",
    version="0.2.6",
    author="zhikh",
    author_email="zhikh.k@gmail.com",
    description="Simple Remote Robot Control Protocol",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/zhikh/s2rcp",
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
