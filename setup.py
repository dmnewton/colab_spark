
from setuptools import setup, find_packages

setup(name='colab_spark',
      version='0.1',
      description='install pysaprk and proxy for ui',
      url='https://github.com/dmnewton/colab_spark',
      author='David Newton',
      author_email='david@example.com',
      license='MIT',
      install_requires=['findspark'],
      packages=find_packages(),
      zip_safe=True)