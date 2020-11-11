from distutils.core import setup

setup(
    name='WA-Testing-Tool',
    version=1.0,
    description='Scripts that run against Watson Assistant for testing intent classification.',
    scripts=[
        'scripts/wa_testing_tool',
        'scripts/download_intents'
    ],
    install_requires=[
        'numpy>=1.13.3',
        'pandas>=0.21',
        'scikit-learn>=0.22.0',
        'scipy>=1.0.0',
        'matplotlib>=2.1.2',
        'aiohttp>=3.4',
        'configparser',
        'squarify>=0.3.0',
        'ibm-watson>=4.0.1',
        'seaborn>=0.9.0',
    ]
)