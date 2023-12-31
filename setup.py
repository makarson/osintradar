import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='osintradar',
    author='makarson',
    version="0.1",
    author_email='makarson@contact.net.tr',
    description='Osintradar free asset malicious checker',
    keywords='osint-radar',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/makarson/osintradar',
    project_urls={
        'Documentation': 'https://github.com/makarson/osintradar',
        'Bug Reports':
        'https://github.com/makarson/osintradar/issues',
        'Source Code': 'https://github.com/makarson/osintradar',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests','validators'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
)
