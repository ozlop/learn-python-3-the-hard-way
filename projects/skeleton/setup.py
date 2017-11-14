try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'desciption': 'My Project',
    'author': 'Ozzy Lopez',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'oswaldo.t.lopez@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
    }

    setup(**config)
