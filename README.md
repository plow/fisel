# fisel
File System Encryption Layer

A set of Python scripts wich recursively encrypt a whole file system directory such that it can be safely copied e.g. to a public cloud storage without relinquish privacy. The encryption ensures that not even the storage provider can analyse your data - neither the the directory structure, nor the filenames, nor the file contents.

## Usage

Encrypt a file:

``export FISEL_KEY=`cat /path/to/encr.key` `` <br />
``cd /path/to/folder`` <br />
``python /dir/to/fisel/fisel_encr.py``

Decrypt a file:

``gpg -d --passphrase `cat /path/to/encr.key` --output out_file.tar --no-use-agent ngiynzmz.tar.gpg``

## Input/Output

To explain what `fisel` does, it's best to go through an example. Let's assume you have the following directory (containing subdirectories and files):

```
$ cd sample_dir
$ tree
.
├── dir0
│   ├── dir00
│   │   ├── file000.txt
│   │   └── file001.txt
│   └── file00.txt
├── dir1
│   ├── file10.txt
│   ├── file11.txt
│   └── file12.txt
└── file.txt
```

The `fisel_encr.py` script generates the following files, encrypts them using the given PGP key and __deletes all orirginal files__:
* A list containing all hashes of all files in `sampple_dir`
* A mappping from the effective subdirectory names (here: `dir0`, `dir1`) to their respective cipher
* A tar ball containing all root-level files (here: `file.txt`)
* A tar ball per subdirectory which is named after its cipher

The hash file looks like this (comments at the beginning are omitted):
```
602,afa64df6ec557330350973899a38562a,./file.txt
7921,34adb92d734615076bef16eecb4e6c61,./dir1/file12.txt
730,08492ef45784e72a65a6c093e4d7fd58,./dir0/dir00/file000.txt
289,144fc93a9bc44870d1f6313657a95cb2,./dir1/file11.txt
0,d41d8cd98f00b204e9800998ecf8427e,./file_hashes.out
2601,ec8c89bfd4fc660f465ef1ec08fbffe2,./dir0/file00.txt
604,45884130034f9c864f98fa8af868e7c7,./dir1/file10.txt
8646,d9048e9664b10ab5c5c2098282230adb,./dir0/dir00/file001.txt
```

And here is the directory mapping file:
```
dir1 -> zgnmnmmy
dir0 -> zmexmtyx
```
At the end, `sample_dir` contains the following files:
```
$ tree
.
├── directory_mapping.out.gpg
├── file_hashes.out.gpg
├── root_files.tar.gpg
├── zgnmnmmy.tar.gpg
└── zmexmtyx.tar.gpg
```