from setuptools import setup

setup(
    name='hervc',
    version='0.3',
    py_modules=['hervc.cli'],
    entry_points={
        'console_scripts': [
            'hervc=hervc.cli:main',
        ],
    },
    author='Herhub Project',
    description='Feminist Git Wrapper CLI',
    long_description='HerVC is a feminist reinterpretation of Git workflows with inclusive language.',
    install_requires=[],
)