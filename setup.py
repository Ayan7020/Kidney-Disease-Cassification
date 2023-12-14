import setuptools 
# For pypi
with open("README.md", "r", encoding="utf-8") as f:
    Long_descrption = f.read()


__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Cassification"
AUTHOR_USER_NAME = "Ayan7020"
SRC_REPO = "CNN_Classifier"
AUTHOR_EMAIL = "ayanshaikh.pr@gmail.com"
 
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for CNN app",
    long_description=Long_descrption,
    Long_descrption_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
