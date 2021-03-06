from setuptools import setup, find_packages
setup(
        name='seqSieve',
        version='0.9.3',
        author='Janina Mass',
        author_email='janina.mass@hhu.de',
        packages=find_packages(),
        scripts=['seqSieve/seqSieve'],
        license='GPLv3',
        url='https://pypi.python.org/pypi/seqSieve/',
        description='Remove outlier sequences from multiple sequence alignment',
        long_description=open('README.txt').read(),
        include_package_data=True,
        install_requires=['numpy', 'matplotlib'],
        classifiers=[
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Topic :: Scientific/Engineering :: Bio-Informatics'
        ],
        )
