from setuptools import setup, find_packages
import sys, os

version = '0.1'

index_fn = os.path.join(os.path.dirname(__file__), 'docs', 'index.txt')

setup(name='DevAuth',
      version=version,
      description="Authentication for developer access to applications",
      long_description=open(index_fn).read(),
      classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Paste",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
      ],
      keywords='wsgi debug tool',
      author='Ian Bicking',
      author_email='ianb@openplans.org',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'WebOb',
        'Paste',
      ],
      entry_points="""
      [paste.app_filter_factory]
      main = devauth.wsgiapp:make_middleware
      """,
      )
