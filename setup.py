from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='replygif',
    version=version,
    description='API client for replygif.net',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='replygif gifs api',
    author='Shaun Duncan',
    author_email='shaun.duncan@gmail.com',
    url='http://www.github.com/shaunduncan/replygif/',
    license='MIT',
    packages=find_packages(),
    py_modules=['replygif'],
    install_requires=['requests'],
)
