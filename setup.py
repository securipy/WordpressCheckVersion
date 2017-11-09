from distutils.core import setup

setup(
    name='WordpressCheckVersion',
    version='0.1.0',
    packages=['wordpresscheckversion'],
    install_requires=['bs4', 'beautifulsoup4', 'lxml'],
    url='https://github.com/securipy/WordpressCheckVersion',
    license='GPL',
    author='goldrak',
    author_email='goldrak@gmail.com',
    description='Python class to process html to detect wordpress version',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.5',
    ]
)
