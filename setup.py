from setuptools import find_namespace_packages, setup

setup(
    name='usefull',
    version='0.1',
    description='Сортування папок',
    url="https://github.com/fghdxfvdxfvdf/DZ_7_2",
    author="Максим Гребеніченко",
    author_email='',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})