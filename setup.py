from setuptools import setup


setup(name='Shrestha Python Package',
      version='0.1',
      description='Read a matrix and run BLAST search',
      url='TBD',
      author='Pawan Shrestha',
      author_email='pawan.shrestha@selu.edu',
      license='MIT',
      packages=['shresthapythonpackage'],
      install_requires=[
          'dendropy',
          'pandas' ,
          'biopython'
      ],
      long_description=open('README.txt').read(),
zip_safe=True)


