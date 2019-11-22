import setuptools
import os.path
from setuptools.command.install import install

executables = {'preprocessing': 'Preprocessing',
               'mcr_als': 'MCR-ALS',
               'clustering': 'Clustering'}

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        print('Running post-install desktop shortcut setup')
        from pyshortcuts import make_shortcut
        proj = 'OCTAVVS '
        for cmd, nom in executables.items():
            make_shortcut(os.path.join(self.prefix, 'bin', 'oct_'+cmd),
                          name=proj+nom, icon='octavvs/icons/preppy.ico',
                          startmenu=False, terminal=True, desktop=True)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="octavvs-ctroein",
    version="0.0.14",
    author="Syahril Siregar, Carl Troein, Michiel Op De Beeck et al.",
    author_email="carl@thep.lu.se",
    description="Open Chemometrics Toolkit for Analysis and Visualization of Vibrational Spectroscopy data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://miccs.info",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numpy', 'scipy', 'matplotlib', 'sklearn',
        'statsmodels', 'pyshortcuts', 'opencv-python'],
    extras_require={'noconda': ['pyqt5']},
    include_package_data = True,
    package_data={ '': ['*.ui', '*.mat', '*.ico'] },
    entry_points={'console_scripts':
        ['oct_preprocessing = octavvs.preprocessing:main',
        'oct_mcr_als = octavvs.mcr_als:main',
        'oct_clustering = octavvs.clustering:main',
        'oct_make_icons = octavvs.make_icons:main'],
    },
#    cmdclass={'install': PostInstallCommand},

)