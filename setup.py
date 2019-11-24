from setuptools import setup, find_packages
assets_requires = [
    'coverage==4.4.2'
]
tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-flakes',
    'pytest-mock==0.9.0',
    'pytest-pep8',
    'pytest-xdist',
    'coverage==4.4.2'
]

setup(
    # Application name:
    name="parkinglot",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="virender bhargav",
    author_email="raif.viren@gmail.com",

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    # Details
    #url="http://pypi.python.org/pypi/parkinglot_v010/",

    #
    # license="LICENSE.txt",
    description="Parking Lot Implementation",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    setup_requires=assets_requires + ["setuptools_git>=0.3"],
    install_requires=assets_requires,

    tests_require=tests_require,
)
