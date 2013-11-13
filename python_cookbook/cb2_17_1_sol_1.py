from distutils.core import setup, Extension
setup(name = "elemlist",
      version = "1.0",
      maintainer = "Alex Martelli",
      maintainer_email = "amcx@aleax.it",
      description = "Sample, simple Python extension module",
      ext_modules = [Extension('elemlist',sources=['elemlist.c'])]
)
