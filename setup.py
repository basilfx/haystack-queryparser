from distutils.core import setup

with open("README.md") as f:
    long_description = f.read()

setup(name='haystack_queryparser',
      version='0.1',
      description='A search query parser that works in conjunction with haystack',
      long_description = long_description,
      author='Vignesh Sarma K',
      author_email='vignesh@recruiterbox.com',
      url='https://github.com/recruiterbox/haystack-queryparser',
      classifiers = [
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
      ],
      keywords = ["parsing", "query", "search"],
      packages = ['haystack_queryparser'],
      )
