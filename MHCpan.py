#!/usr/bin/env python2

"""
this script will help use the netMHCpan Tool

by: Sinai Sacharen

"""

""" imports """
#------------------------------------------------------------------------ <editor-fold>
import sys
import subprocess
import os
#------------------------------------------------------------------------ </editor-fold>

""" paths """
#------------------------------------------------------------------------ <editor-fold>

path_to_tool = '/home/sacharen/netMHCpan-4.1/'
path_with_seq = '/mnt/c/Users/User/Documents/COVID-19/netMHCpan-4.1/'
path_to_save = '/mnt/c/Users/User/Documents/COVID-19/netMHCpan-4.1/'
if os.path.exists(path_to_tool) and os.path.exists(path_to_save) and os.path.exists(path_with_seq):
    print('found all paths  :) ')
else:
    print('cant find a path  :( ')


#------------------------------------------------------------------------ </editor-fold>


""" global variables """
#------------------------------------------------------------------------ <editor-fold>

input_file = path_with_seq+'spike_file.txt'
output_file = path_to_save + 'MHC_out.txt'

# HLA_str = 'HLA-A01:01,HLA-A02:01,HLA-A03:01,HLA-A24:02,HLA-A26:01,HLA-B07:02,HLA-B08:01,HLA-B27:05,HLA-B39:01,HLA-B40:01,HLA-B58:01,HLA-B15:01'
HLA_str = 'HLA-A01:01'

peptide_length= "8,9,10,11" #-l

#------------------------------------------------------------------------ </editor-fold>


""" MAIN """

#------------------------------------------------------------------------ <editor-fold>


command=path_to_tool+"netMHCpan "+ input_file+ " -l "+peptide_length+ " -a "+HLA_str +" -s "+" >"+ output_file


subprocess.check_output('%s' % command, shell=True)



#------------------------------------------------------------------------ </editor-fold>


