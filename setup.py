from setuptools import find_packages, setup

setup(
    name="betty_utils_service",
    description="betty utils service for auth and errors",
    version="0.2.22",
    license="MIT",
    author="Petr Shcherbakov-Sandu",
    author_email="petrscherbakov93@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/petruxa77799/betty_utils_service",
    keywords="betty utils service",
    install_requires=["pyjwt>=2.10.1", "ujson>=5.10.0", "aiokafka>=0.12.0"],
)
