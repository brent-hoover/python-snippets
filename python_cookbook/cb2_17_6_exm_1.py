from distutils.core import setup, Extension
setup(name="total", maintainer="Luther Blissett", maintainer_email=
    "situ@tioni.st", ext_modules=[Extension('total', sources=['total.c'])]
)
