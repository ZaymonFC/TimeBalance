from setuptools import setup

setup(
    name="TimeBalance",
    version='0.1',
    py_modules=['TimeBalance'],
    install_requires=[
        'Click',
        'sqlalchemy'
    ],
    entry_points='''
        [console_scripts]
        TimeBalance=TimeBalance:cli
    ''',
)