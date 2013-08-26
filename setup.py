from setuptools import setup, find_packages

long_description = '\n\n'.join([open('README.md').read()
                                ])


setup(
    name='pandoc-watch',
    version='%%version%%',
    description='pandoc-watch is a watcher running the pandoc command when modifications are made to base files.',
    long_description=long_description,
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Environment :: Console",
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        "Topic :: Software Development",
        "Programming Language :: Python :: 2.5",
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Editors :: Documentation',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Utilities'
    ],
    keywords='pandoc watcher',
    py_modules=['pandocwatch'],
    author='David Loureiro',
    author_email='david.loureiro1@gmail.com',
    url='https://github.com/dloureiro/pandoc-watch',
    license='GNU AGPL v3',
    install_requires=[
        'setuptools',
        'watchdog'
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    [console_scripts]
    pandoc-watch = pandocwatch:main
    """,
)
