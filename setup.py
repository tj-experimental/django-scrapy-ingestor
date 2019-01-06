from setuptools import setup


setup(
    name='django-scrapy-ingestor',
    install_requires=['python-twitter==3.5'],
    extras_require={
        'development': ['pip-tools==3.2.0'],
        'tests': ['coverage', 'pytest'],
        'docs': [],
    }
)
