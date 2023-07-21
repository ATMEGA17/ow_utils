#!/usr/bin/env python
import os
import sys

from openwisp_utils import get_version
from setuptools import find_packages, setup

if sys.argv[-1] == 'publish':
    # delete any *.pyc, *.pyo and __pycache__
    os.system('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload -s dist/*")
    os.system("rm -rf dist build")
    args = {'version': get_version()}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    install_requires=[
        'django-model-utils~=4.3.1',
        'django-compress-staticfiles~=1.0.1b',
        'django-admin-autocomplete-filter~=0.7.1',
        'swapper~=1.3.0',
    ],
    extras_require={
        'qa': [
            'black~=22.3.0',
            'flake8<=3.9',
            'isort~=5.0',
            'readme-renderer~=28.0',
            'coveralls~=3.0.0',  # depends on coverage as well
            'tblib~=1.7',
        ],
        'rest': [
            'djangorestframework~=3.14.0',
            'django-filter~=23.2',  # django-filter uses CalVer
            # The coreapi package is archived and all packages
            # are moving away from coreapi (e.g. DRF, django-filter, drf-yasg).
            # There's already an open PR in drf-yasg
            # https://github.com/axnsan12/drf-yasg/pull/857.
            # TODO: Before releasing, check if newer version
            # of drf-yasg is available.
            'drf-yasg[coreapi]~=1.21.0',
        ],
        'celery': ['celery~=5.3.0'],
        'selenium': ['selenium~=4.10.0'],
    },
)