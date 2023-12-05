from setuptools import find_packages, setup


setup(
    name='adventofpy',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==8.1.7',
    ],
    entry_points={
        'console_scripts': [
            'adventofpy = adventofpy:cli',
        ],
    },
)
