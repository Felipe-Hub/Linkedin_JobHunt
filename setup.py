import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="job_hunter",
    version="0.0.1",
    author="Felipe Rocha",
    author_email="felipe.chaves.rocha@gmail.com",
    description="Packages setup for job_hunter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Felipe-Hub/Linkedin_JobHunt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux :: Ubuntu 20.0",
        ],
    python_requires='>=3.7',
)