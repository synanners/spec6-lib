from google.appengine.ext import vendor
import os,sys
import tempfile
tempfile.SpooledTemporaryFile = tempfile.TemporaryFile

vendor.add('lib')

if os.name == "nt":
    os.name = ""
    sys.platform = ""