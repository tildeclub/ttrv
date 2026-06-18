import setuptools

from ttrv.__version__ import __version__ as version


install_requires = [
    'beautifulsoup4',
    'decorator',
    'kitchen',
    'requests >=2.4.0',  # https://github.com/tildeclub/ttrv/issues/325
    'six',
]

tests_require = [
    'coveralls',
    'pytest>=8.3.0',
    'coverage',
    'mock',
    'pylint',
    'vcrpy',
]

extras_require = {
    'test': tests_require
}

def long_description():
    with open('README.md', encoding='utf8') as f:
        return f.read()


setuptools.setup(
    name='ttrv',
    version=version,
    description='Tilde Terminal Reddit Viewer',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/tildeclub/ttrv',
    author='deepend (forked from RTV)',
    author_email='deepend@tilde.club',
    license='MIT',
    keywords='reddit terminal praw curses',
    packages=[
        'ttrv',
        'ttrv.packages',
        'ttrv.packages.praw'
    ],
    package_data={
        'ttrv': ['templates/*', 'themes/*'],
        'ttrv.packages.praw': ['praw.ini']
    },
    data_files=[("share/man/man1", ["ttrv.1"])],
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires='>=3.9',
    entry_points={'console_scripts': ['ttrv=ttrv.__main__:main']},
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console :: Curses',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Topic :: Terminals',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        ],
)
