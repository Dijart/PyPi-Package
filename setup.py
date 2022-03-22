from setuptools import setup, find_packages


setup(
    name='PyPi-Package',
    version='0.6',
    license='MIT',
    author="Dijart Haliti",
    author_email='dijarthaliti@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Dijart/PyPi-Package.git',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)
