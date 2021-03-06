# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup

setup(name='SeleniumProxy',
      version='0.1.0',
      description='A shim that allows the use of Selenium Bindings with Marionette',
      author='David Burns',
      author_email='dburns at mozilladotcom',
      url='https://github.com/AutomatedTester/Selenium-Proxy',
      classifiers=['Development Status :: 3 - Alpha',
                  'Intended Audience :: Developers',
                  'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
                  'Operating System :: POSIX',
                  'Operating System :: Microsoft :: Windows',
                  'Operating System :: MacOS :: MacOS X',
                  'Topic :: Software Development :: Testing',
                  'Topic :: Software Development :: Libraries',
                  'Programming Language :: Python'],
      py_modules=['selenium_proxy'],
      # TODO(David) add Marionette when that is up on Pypi
      install_requires=["mozrunner==5.2","mozprofile==0.2", "selenium"]
      )
