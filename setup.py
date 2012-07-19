from distutils.core import setup

setup(name='Canto',
      version='0.8.0',
      description='Next-gen console RSS/Atom reader',
      author='Jack Miller',
      author_email='jack@codezen.org',
      url='http://codezen.org/canto',
      packages=['canto_next'],
      scripts=['bin/canto-daemon','bin/canto-remote'],
      data_files = [("share/man/man1/", ["man/canto-daemon.1", "man/canto-remote.1"])],
     )
