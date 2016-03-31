from setuptools import setup
from steganography import __version__
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name='steganography',
    version=__version__,
    description="'My Number' validate module",
    long_description=long_description,
    author='haminiku',
    author_email='haminiku1129@gmail.com',
    url='https://github.com/subc/steganography',
    packages=['steganography'],
    package_dir={'steganography': 'steganography'},
    include_package_data=True,
    install_requires=[],
    license='MIT License',
    zip_safe=False,
    keywords=["Implementation Hide Text In Image with encryption", "stegano", "steganography"],
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ),

)