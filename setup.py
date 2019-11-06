import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='brcomarcas',
    version="0.0.4",
    author='Iasmini Gomes',
    author_email='iasmini.gomes@gmail.com',
    description='Functions to list court districts of Brazil',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/iasmini/brcomarcas',
    packages=setuptools.find_packages(),
    keywords=['brasil', 'brazil', 'comarca', 'comarcas'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3',
)
