from distutils.core import setup

INSTALL_REQUIRES = ['bs4', 'beautifulsoup4','lxml']


setup(
    name='WordpressCheckVersion',
    version='0.1.0',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    url='https://github.com/securipy/WordpressCheckVersion',
    license='GPL',
    author='goldrak',
    author_email='goldrak@gmail.com',
    description='Python class to process html to detect wordpress version',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPL License',
        'Programming Language :: Python :: 3.5',
    ]
)