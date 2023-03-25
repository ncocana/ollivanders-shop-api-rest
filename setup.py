from setuptools import setup, find_packages

setup(
    name="Ollivanders Shop API Rest",
    version="1.0",
    author="ncocana",
    url="https://github.com/ncocana/ollivanders-shop-api-rest",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "attrs==22.2.0",
        "bandit==1.7.5",
        "black==23.1.0",
        "cachetools==5.3.0",
        "certifi==2022.12.7",
        "chardet==5.1.0",
        "charset-normalizer==3.1.0",
        "click==8.1.3",
        "colorama==0.4.6",
        "coverage==7.2.2",
        "distlib==0.3.6",
        "docopt==0.6.2",
        "exceptiongroup==1.1.1",
        "filelock==3.10.4",
        "Flask==2.2.3",
        "gitdb==4.0.10",
        "GitPython==3.1.31",
        "idna==3.4",
        "iniconfig==2.0.0",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.2",
        "markdown-it-py==2.2.0",
        "MarkupSafe==2.1.2",
        "mdurl==0.1.2",
        "mypy-extensions==1.0.0",
        "packaging==23.0",
        "pathspec==0.11.1",
        "pbr==5.11.1",
        "platformdirs==3.1.1",
        "pluggy==1.0.0",
        "Pygments==2.14.0",
        "pyproject_api==1.5.1",
        "pytest==7.2.2",
        "PyYAML==6.0",
        "requests==2.28.2",
        "rich==13.3.2",
        "smmap==5.0.0",
        "stevedore==5.0.0",
        "tomli==2.0.1",
        "tox==4.4.7",
        "urllib3==1.26.15",
        "virtualenv==20.21.0",
        "Werkzeug==2.2.3",
        "yarg==0.1.9",
    ],
)
