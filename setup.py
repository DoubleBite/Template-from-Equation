import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='template_from_equation',  
    version='0.1',
    author="Shih-hong Tsai",
    author_email="doublebite@iis.sinica.edu.tw",
    description="Create template from equation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doubleBite/Template-from-Equation",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
 )