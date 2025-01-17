import setuptools
import sys


requirements = ['selenium', 'requests', 'selenium-interceptor', "undetected-chromedriver", "selenium-wire", "webdriver-manager", "selenium-injector>=2.3"]

if 'google.colab' in sys.modules: # we're on google-colab
    requirements.extend(['PyVirtualDisplay', "google-colab-shell"])

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='selenium_profiles',
    author='Aurin Aegerter',
    author_email='aurinliun@gmx.ch',
    description='Emulate and Automate Chrome using Profiles and Selenium',
    keywords='Selenium,emulation, automation, undetected-chromedriver, webautomation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kaliiiiiiiiii/Selenium_Profiles',
    project_urls={
        'Documentation': 'https://github.com/kaliiiiiiiiii/Selenium_Profiles',
        'Bug Reports':
            'https://github.com/kaliiiiiiiiii/Selenium_Profiles/issues',
        'Source Code': 'https://github.com/kaliiiiiiiiii/Selenium_Profiles',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: Free for non-commercial use',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Framework :: Jupyter',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Browsers',

    ],
    python_requires='>=3.7',
    install_requires=requirements,
    include_package_data=True,
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
)
