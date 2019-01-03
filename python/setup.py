from setuptools import setup

setup(
    name='example',
    version='0.0.1',
    packages=['example'],
    entry_points={
        'console_scripts': [
            'example_server=example:server',
        ],
    },
    setup_requires=['pytest-runner'],
    install_requires=['Flask'],
    tests_require=['pytest'],
    test_suite='tests',
    url='',
    license='',
    author='Mark Shroyer',
    author_email='mark@shroyer.name',
    description='An example Python Docker application',
)
