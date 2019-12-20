import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-press',
    version='0.1.1',
    packages=find_packages(exclude=('pysite', 'media', 'venv', 'static')),
    tall_requires=['django', ],
    include_package_data=True,
    license='MIT License',
    description='Easy start web app without coding',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/YutaUra/YCU-Programing/tree/master/Code_Review/ura_1',
    author='Yuta Ura',
    author_email='yuuta3594@outlook.jp',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Japanese',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
