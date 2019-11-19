from setuptools import setup

setup(
    name="usfm_tools",
    version="0.0.31",
    author="unfoldingWord",
    author_email="info@unfoldingWord.org",
    description="A framework for transforming .usfm files into specified targets",
    license="MIT",
    keywords="unfoldingWord usfm tools",
    url="https://github.com/unfoldingWord-dev/USFM-Tools",
    packages=['usfm_tools', 'usfm_tools/support'],
    long_description='This project comprises a framework for transforming .usfm files into specified targets. It is '
                     'primarily used for the Open English Bible, and may need adjustment if used for other purposes. '
                     'This fork of USFM-Tools includes basic support for conversion to USX.',
    classifiers=[],
    install_requires=[
        'bs4==0.0.1',
        'coveralls==1.8.2',
        'future==0.18.2',
        'pyparsing==2.4.5'
    ],
    test_suite='tests'
)
