from setuptools import find_packages, setup

setup(
    name='intension',
    packages=find_packages(include=['intension']),
    version='0.1.0',
    description='Intension library for Python',
    author='Daniel Malo Osorio',
    license='GPL v3',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.1.2'],
    test_suite='tests',
)