import os
import re
import hashlib

dirmap_file = 'directory_mapping.out'
rootfile_dir = 'root_files'

# Returns first 8 characters of the Base64-to-lowercase encoded MD5 hash of the input filename.
def get_md5_short(fname):
    hash = hashlib.md5()
    hash.update(fname)
    return hash.hexdigest().encode('base64').strip().lower()[0:8]


# Appends a mapping from an original path to the new (obfuscated) path.
def append_mapping(origname, newname):
    with open(dirmap_file, 'a') as foldermap:
        mapping = origname + ' -> ' + newname
        #print "  " + mapping
        foldermap.write(mapping + '\n')



############# MAIN OBFUSCATION PROCEDURE ##############

def obfuscate(hashdeep_file):

    # Check for an already existing directory mapping file. Delete it if it exists.
    if os.path.isfile(dirmap_file):
        os.remove(dirmap_file)
        print 'Removed existing folder mapping ' + dirmap_file


    for i in os.listdir(os.getcwd()):
        if os.path.isdir(i):
	    # search for date prefix in dir name: accepts formats 20160324-... and 2016-03-24-... 
            m = re.search('^(19|20)\d{2}\-?(0[1-9]|1[0-2])\-?(0[1-9]|[1-2]\d|3[0-1])\-?', i)
            if m:
                newname =  m.group(0) + get_md5_short(i)
	    else:
		newname = get_md5_short(i)
	    append_mapping(i, newname)
            os.rename(i, newname)        
	    continue
        else:
            rootfile_dir_path = os.getcwd() + "/" + rootfile_dir
            if not os.path.exists(rootfile_dir_path):
                os.makedirs(rootfile_dir_path)
                print 'Created directory for root-level files: ' + rootfile_dir_path
            if not i == hashdeep_file:            
                os.rename(i, rootfile_dir + '/' + i)
                #print 'Moved ' + i + ' to ' + rootfile_dir

    print 'Finished obfuscating directory names.'
