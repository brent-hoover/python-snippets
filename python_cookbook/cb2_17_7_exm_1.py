from distutils.core import setup, Extension
setup(name="totit", maintainer="Luther Blissett", maintainer_email=
    "situ@tioni.st", ext_modules=[Extension('totit', sources=['totit.c'])]
)
