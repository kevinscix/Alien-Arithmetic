import glob
import os

"""
Generate the code documentation, using pydoc.
"""

for dirname in ['components', 'Interface']:
    print(dirname)
    flist = glob.glob(os.path.join(dirname, '*.py'))
    print(flist)
    for fname in flist:
        print(fname)
        if not fname.endswith('__init__.py'):
            os.system('python -m pydoc -w %s' % fname)
            bname = os.path.splitext(os.path.basename(fname))[0]  
            os.system('mv %s.html %s.%s.html' % (bname, dirname, bname))
    os.system('python -m pydoc -w %s' % dirname)
os.system('mv *.html docs')