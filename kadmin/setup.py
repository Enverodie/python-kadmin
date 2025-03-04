#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

from setuptools.extension import Extension
from distutils.util import execute, newer
from distutils.spawn import spawn


def setup():

    #
    # hack to support linking when running
    #  python setup.py sdist
    #
    import os
    if hasattr(os, 'link'):
        del os.link

    if newer('./src/getdate.y', './src/getdate.c'):
        execute(spawn, (['bison', '-y', '-o', './src/getdate.c', './src/getdate.y'],))

    execute(spawn, (['mkdir', '-p', './build/bdist.linux-x86_64/wheel'],))

    setuptools.setup(
        name='kadmin',
        version='0.0.3',
        description='Python module for kerberos admin (kadm5)',
        url='https://github.com/nightfly19/python-kadmin',
        download_url='https://github.com/nightfly19/python-kadmin/tarball/v0.0.2',
        author='Russell Jancewicz, Sage Imel',
        author_email='sageimel@gmail.com',
        python_requires='>=3.8.5',
        license='MIT',
        ext_modules=[
            Extension(
                "kadmin",
                libraries=["krb5", "kadm5clnt", "kdb5"],
                include_dirs=["/usr/include/", "/usr/include/et/"],
                sources=[
                    "src/kadmin.c",
                    "src/PyKAdminErrors.c",
                    "src/PyKAdminObject.c",
                    "src/PyKAdminIterator.c",
                    "src/PyKAdminPrincipalObject.c",
                    "src/PyKAdminPolicyObject.c",
                    "src/PyKAdminCommon.c",
                    "src/PyKAdminXDR.c",
                    "src/getdate.c"
                ],
            )
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: System Administrators",
            "Intended Audience :: Developers",
            "Operating System :: POSIX",
            "Programming Language :: C",
            "Programming Language :: Python",
            "Programming Language :: YACC",
            "License :: OSI Approved :: MIT License",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: System :: Systems Administration :: Authentication/Directory",
        ]
    )


setup()