import setuptools

setuptools.setup(
    name="JSON-Chunker",
    author="Dogukan Ertunga Kurnaz",
    version="1.0.0",
    description="A little helper tool to split big json files into chunks",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    url="https://github.com/DogukanK/JSON-Chunker",
    python_requires=">=3.6",

)
