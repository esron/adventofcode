from setuptools import setup


setup(
    name='adventofpy',
    versrion='0.1.0',
    py_modules=['adventofpy'],
    install_requires=[
        'click==8.0.4',
    ],
    entry_points={
        'console_scripts': [
            'adventofpy = adventofpy:cli',
        ],
    },
)
