import setuptools
import codecs

with codecs.open('README.md', 'r', 'utf_8') as readme:
    long_description = readme.read()

setuptools.setup(
    name = 'phenrsteno',
    version = '0.0.1',
    author = 'Gregory Chamberlain',
    author_email = '15685804+contrum@users.noreply.github.com',
    description = 'Phonemic non-rhotic English stenotype system for Plover',
    License = 'GNU General Public License v2 or later (GPLv2+)',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/contrum/phenrsteno',
    packages = setuptools.find_packages(),
    classifiers = (
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop',
    ),
    install_requires =[
        'plover>=4.0.0.dev0',
    ],
    py_modules = [
        'plover_phenr',
    ],
    entry_points = '''

[plover.system]
Phenrsteno = plover_phenr

''',
    zip_safe = True,
)
