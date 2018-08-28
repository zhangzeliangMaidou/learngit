'''
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-p", "--pdbk",action="store_true",dest="pdcl",default=False,help="write pdbk data to oracle db")
parser.add_option("-z", "--zdbk",action="store_true",dest="zdcl",default=False,help="write zdbk data to oracle db")
(options, args) = parser.parse_args()

if options.pdcl==True:
    print ('pdcl is true')
if options.zdcl==True:
    print ('zdcl is true')
'''
from optparse import OptionParser
import os
import sys
[...]
parser = OptionParser()
parser.add_option("-f","--file",dest="filename",help="write report to FILE",metavar="FILE")
parser.add_option("-q","--quiet",action="store_false",dest="verbose",default=True,help="don't print status message to stdout")
(options,args) = parser.parse_args()
print (options.filename)

if options.filename is not None:
    if not os.path.isdir(sys.path[0]+os.sep+options.filename):
        print ("OKKK")
        os.makedirs(sys.path[0]+os.sep+options.filename)
    else:
        print("%s Exists"%options.filename)
else:
    print ("KO")
        

