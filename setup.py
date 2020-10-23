import atexit
import sys
import os

from setuptools import setup, find_packages
from setuptools.command.develop import develop


class Develop(develop):
    def run(self):
        pkn = self.config_vars.get('dist_name')

        def _post_install():
            def find_module_path():
                for p in sys.path:
                    if os.path.isdir(p) and pkn in os.listdir(p):
                        return os.path.join(p, pkn)

            from subprocess import call
            call(['yarn'], cwd=find_module_path())

        atexit.register(_post_install)
        develop.run(self)


setup(
    name='flask-admin-lte',
    packages=find_packages(),
    version='0.2',
    description='Integrates LteAdmin into flask-admin',
    author='Alex Belyaev',
    author_email='a.v.belyaev@gmail.com',
    cmdclass={'develop': Develop},
    install_requires=[
        'flask-admin>=1.4.0'
    ],
)
