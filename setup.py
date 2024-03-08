import sys
import codecs
import setuptools

from version import __version__ as version


install_requires = [
    'beautifulsoup4',
    'decorator',
    'kitchen',
    'requests >=2.4.0',  # https://github.com/tildeclub/ttrv/issues/325
    'six',
]

tests_require = [
    'coveralls',
    'pytest>=3.1.0',  # Pinned for the ``pytest.param`` method
    'coverage',
    'mock',
    'pylint',
    'vcrpy',
]

extras_require = {
    'test': tests_require
}

# https://hynek.me/articles/conditional-python-dependencies/
if int(setuptools.__version__.split(".", 1)[0]) < 18:
    assert "bdist_wheel" not in sys.argv
    if sys.version_info[0:2] < (3, 6):
        install_requires.append("mailcap-fix")
else:
    # Building the bdist_wheel with conditional environment dependencies
    # requires setuptools version > 18. For older setuptools versions this
    # will raise an error.
    extras_require.update({":python_version<'3.6'": ["mailcap-fix"]})


def long_description():
    with codecs.open('README.md', encoding='utf8') as f:
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
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={'console_scripts': ['ttrv=ttrv.__main__:main']},
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console :: Curses',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Terminals',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        ],
)
