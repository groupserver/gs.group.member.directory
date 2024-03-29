# coding=utf-8
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.group.member.directory',
    version=version,
    description="Group Membership content provider",
    long_description=open("README.rst").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.rst")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='group membership group groupserver',
    author='Richard Waid',
    author_email='richard@onlinegroups.net',
    url='http://www.onlinegroups.net/',
    license='other',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group', 'gs.group.member'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'Products.GSGroup',
        'Products.GSGroupMember',
        'gs.group.member.base',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)

