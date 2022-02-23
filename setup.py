from setuptools import find_packages, setup


setup(
    name='adventofpy',
    versrion='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==8.0.4',
    ],
    entry_points={
        'console_scripts': [
            'adventofpy = adventofpy:cli',
        ],
    },
)
