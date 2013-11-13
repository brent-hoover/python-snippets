from distutils.core import setup, Extension
from Pyrex.Distutils import build_ext
setup(name = "elemlist",
      version = "1.0",
      maintainer = "Alex Martelli",
      maintainer_email = "amcx@aleax.it",
      description = "Simple Python extension module in Pyrex",
      ext_modules = [Extension('elemlist',sources=['elemlist.pyx'])],
      cmdclass = {'build_ext': build_ext},
)
