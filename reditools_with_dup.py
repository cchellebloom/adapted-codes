###### this is a very simple modification to REDItools3 RNA editing identification function, which inherently does not keep reads with FLAGs that have been changed due to being marked as duplicates. I wanted the option to keep duplicates and compare, just in case duplicate removal might impact RNA editing analysis
## to run it:
# python -m reditools.reditools_with_dup analyze [bam file] -o [out file]

import runpy
import sys

from reditools.alignment_file import ReadQC

# Include duplicate-marked versions of the normally accepted SAM flags
ReadQC._flags_to_keep = ReadQC._flags_to_keep | {
    flag | 0x400 for flag in ReadQC._flags_to_keep
}

# Run REDItools3's normal command-line interface
sys.argv[0] = "reditools"
runpy.run_module("reditools", run_name="__main__", alter_sys=True)
