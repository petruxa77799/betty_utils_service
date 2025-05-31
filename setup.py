from setuptools import setup, find_packages


setup(
    name="betty_utils_service",
    description="betty utils service for auth and errors",
    version="0.0.1",
    license="MIT",
    author="Petr Shcherbakov-Sandu",
    author_email="petrscherbakov93@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/petruxa77799/betty_utils_service",
    keywords="betty utils service",
    install_requires=["pyjwt==2.10.1"],
)
