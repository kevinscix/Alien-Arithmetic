import glob
import os

"""
Generate the code documentation, using pydoc.
"""

for dirname in ['components', 'Interface']:
    flist = glob.glob(os.path.join(dirname, '*.py'))
    for fname in flist:
        print(fname)
        if not fname.endswith('__init__.py'):
            os.system('python3 -m pydoc -w %s' % fname)
            bname = os.path.splitext(os.path.basename(fname))[0]  
            os.system('mv %s.html %s.%s.html' % (bname, dirname, bname))
    os.system('python3 -m pydoc -w %s' % dirname)
os.system('mv *.html docs')