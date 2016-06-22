import os
import glob
from setuptools import setup, find_packages

src_dir = os.path.dirname(__file__)

install_requires = [
    'PyYAML>=3.11',
    # Lock to a specific version of stacker & stacker_blueprints so there are
    # no surprises
    'stacker==0.6.3',
    'stacker_blueprints==0.6.5',
    'awacs>=0.5.4',
    'troposphere>=1.5.0'
]

tests_require = (
    'nose>=1.0',
    'mock==1.0.1',
)


if __name__ == '__main__':
    setup(
        name='example_blueprints',
        version='0.1.0',
        author='Michael Barrett',
        author_email='loki77@gmail.com',
        license="New BSD license",
        url="https://github.com/phobologic/example_stacks",
        description='Example package for laying out stacker stacks',
        install_requires=install_requires,
        tests_require=tests_require,
        test_suite='nose.collector',
        packages=find_packages(),
        scripts=glob.glob(os.path.join(src_dir, 'bin', 'scripts', '*'))
    )
