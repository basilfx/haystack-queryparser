from setuptools import setup

setup(
    name='haystack_queryparser',
    version='0.3.0',
    description='A search query parser that works in conjunction with Django Haystack.',  # noqa
    author='Vignesh Sarma K',
    author_email='vignesh@recruiterbox.com',
    url='https://github.com/Aplopio/haystack-queryparser',
    download_url='https://github.com/Aplopio/haystack-queryparser/releases/download/v0.2.1/haystack_queryparser-0.2.1.tar.gz',  # noqa
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    keywords=["parsing", "query", "search"],
    packages=['haystack_queryparser'],
    setup_requires=["nose"],
    install_requires=["django-haystack"],
    test_suite="tests",
    zip_safe=False
)
