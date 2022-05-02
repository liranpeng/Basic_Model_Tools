

import os
import sys
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import glob
from configargparse import ArgParser
import argparse

def lonlat_in(lat, lon, lat1, lon1, lat2, lon2):
    flag = 0
    if lon >lon1:
        if lon <lon2:
            if lat >lat1:
                if lat <lat2:
                    flag = 1
    return flag

# Python program to check if two
# to get unique values from list
# using traversal
 
# function to get unique values
def unique(list1):
     
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list


def preprocess(argument):
    """
    This is the main script that preprocesses one file.

    Returns
    -------

    """
    from os import path

    indir = argument.in_dir[:]
    infile = argument.in_filesample[:]

    lonll  = argument.lon_lowleft
    latll  = argument.lat_lowleft
    lonur  = argument.lon_upright
    latur  = argument.lat_upright
    rname  = argument.Region_Name[:]
    corem  = argument.core_max
    flagc  = argument.cross360
    ftype  = argument.in_filetype[:]

    #indir = argument.in_dir
    #infile = argument.in_filesample
    #rname  = argument.Region_Name
    #ftype  = argument.in_filetype
    print('========================')
    print('Input directory: '+indir)
    print('Input file: '+infile)
    print('Lower left lon: '+str(lonll))
    print('Lower left lat: '+str(latll))
    print('Upper right lon: '+str(latur))
    print('Upper right lat: '+str(lonur))
    print('Region Name: '+rname)
    print('File Type: '+ftype)
    print('Maximum Core: '+str(corem))
    print('========================')
    if indir=='None': logging.debug(f'No in_dir so in_fns is set to in_fns')
   
    #print('Liran Here')
    print(indir)
    #print('Liran Here2')

    SP2008 = xr.open_mfdataset(indir+'*frontera.cam.'+(ftype)+'.2008-10-01-00000.nc')

    lon = SP2008.lon.values
    lat = SP2008.lat.values
    OCNFRAC = SP2008.OCNFRAC.isel(time=0).values
    if flagc==1:
        ind_Peruvian = [-999]        
        for il in range(len(lon)):
            #d0 = lonlat_in(lat[il], lon[il],-20,0,0,20) # Namibian
            d0 = lonlat_in(lat[il], lon[il],latll,0,latur,lonur) # Namibian
            if OCNFRAC[il]>0.95:
                if d0>0:
                    ind_Peruvian.append(il)

            #d0 = lonlat_in(lat[il], lon[il],-20,350,0,360) # Namibian
            d0 = lonlat_in(lat[il], lon[il],latll,lonll,latur,360) # Namibian
            if OCNFRAC[il]>0.95:
                if d0>0:
                    ind_Peruvian.append(il)
    if flagc==0:
        ind_Peruvian = [-999]
        for il in range(len(lon)):
            #d0 = lonlat_in(lat[il], lon[il],-30,265,-8,290) # Peruvian
            #print(latll,lonll,latur,lonur)
            d0 = lonlat_in(lat[il], lon[il],latll,lonll,latur,lonur)
            if OCNFRAC[il]>0.5:
                if d0>0:
                    ind_Peruvian.append(il)

    ind_Peruvian0 = ind_Peruvian[1:]
    #print(ind_Peruvian)
    ind_Peruvian = unique(ind_Peruvian0)
     
    Region_Path = indir+rname+'_Run'
    cmd = 'rm -rf '+ Region_Path
    os.system(cmd)
    
    cmd = 'mkdir '+ Region_Path
    os.system(cmd)
    
    f6 = open(Region_Path+'/'+'Run_main'+(ftype)+'.sh',"w")
    f6.write('#!/bin/bash')
    f6.write('\n')
    f6.write('#SBATCH -J myjob_'+rname+'           # Job name')
    f6.write('\n')
    f6.write('#SBATCH -o myjob_'+rname+'.o%j       # Name of stdout output file')
    f6.write('\n')
    f6.write('#SBATCH -e myjob_'+rname+'.e%j       # Name of stderr error file')
    f6.write('\n')
    f6.write('#SBATCH -p small           # Queue (partition) name')
    f6.write('\n')
    f6.write('#SBATCH -N 1               # Total # of nodes (must be 1 for serial)')
    f6.write('\n')
    f6.write('#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)')
    f6.write('\n')
    f6.write('#SBATCH -t 48:00:00        # Run time (hh:mm:ss)')
    f6.write('\n')
    f6.write('#SBATCH --mail-type=all    # Send email at begin and end of job')
    f6.write('\n')
    f6.write('#SBATCH -A ATM20009       # Project/Allocation name ')
    f6.write('\n')
    f6.write('#SBATCH --mail-user=liranp@uci.edu')
    f6.write('\n')
    f6.write('chmod 700 *.sh')
    f6.write('\n')
    f6.write('module load nco')
    f6.write('\n')

    f4 = open(Region_Path+'/Step1_'+'0Run_main'+(ftype)+'.sh',"w")
    f6.write('./Step1_'+'0Run_main'+(ftype)+'.sh')
    f6.write('\n')
    f4.write('#!/bin/bash')
    f4.write('\n')
    f4.write('chmod 700 *.sh')
    f4.write('\n')
    f4.write('module load nco')
    f4.write('\n')
    corecount = 0
    splitcount = 0
    fcount = 0
    coremax = corem
    print('Max Core '+str(coremax))
    for filename in glob.iglob(f'{indir}*.cam.'+(ftype)+'.2008-10-*.nc'):
        print(filename)
        SP_Case = filename[len(filename)-len(infile):len(filename)]
        
        Date_Time = SP_Case[len(SP_Case)-19:len(SP_Case)-3]
        indexstr = (ind_Peruvian)
        
        
        f4.write('./'+'step1_runsplit-'+Date_Time+(ftype)+'.sh&')
        corecount = corecount+1
        print('Here test '+str(corecount))
        f4.write('\n')
        if corecount==coremax:
            f4.close() 
            fcount = fcount + 1
            f4 = open(Region_Path+'/Step1_'+str(fcount)+'Run_main'+(ftype)+'.sh',"w")
            f6.write('./Step1_'+str(fcount)+'Run_main'+(ftype)+'.sh')
            f6.write('\n')
            f4.write('#!/bin/bash')
            f4.write('\n')
            f4.write('chmod 700 *.sh')
            f4.write('\n')
            f4.write('module load nco')
            f4.write('\n')
            corecount = 0
        
        f3 = open(Region_Path+'/'+'step2_runcombine-'+Date_Time+(ftype)+'.sh',"w")
        f3.write('#!/bin/bash')
        f3.write('\n')
        f3.write('ncra ')
        f2 = open(Region_Path+'/'+'step1_runsplit-'+Date_Time+(ftype)+'.sh',"w")
        f2.write('#!/bin/bash')
        f2.write('\n')
        f2.write('cd '+Region_Path)
        f2.write('\n')
        f2.write('./'+str(0)+'run_split-'+Date_Time+(ftype)+'.sh')
        f2.write('\n')
        #print(str(0)+'run_split-'+Date_Time+'.sh')
        f = open(Region_Path+'/'+str(0)+'run_split-'+Date_Time+(ftype)+'.sh',"w")
        f.write('#!/bin/bash')
        f.write('\n')
        for il in range(len(indexstr)):
            cmd = 'cd '+indir
            os.system(cmd)
            
            SP_Case2 = SP_Case[0:len(SP_Case)-3]+'_'+str(indexstr[il])+'_'+rname+'_split_'+(ftype)+'.nc'
            splitcount = splitcount + 1
            f3.write(SP_Case2+' ')
                
            evalstring = 'ncea -F -d ncol,'+str(indexstr[il])+' ' +indir+ SP_Case+' '+Region_Path+'/'+SP_Case2 +' ' #& 
            f.write(evalstring)
            f.write('\n')

        #UPhy = eval(evalstring)
        f3.write(Date_Time+rname+'_mean_'+(ftype)+'.nc')
        f3.write('\n')
        #f3.write('rm *'+rname+'_split.nc')
        f3.write('\n')
        #f3.write('rm '+'*run_split-'+Date_Time+'.sh')
        
        f3.close() 
        f2.close()   
        f.close()
    f4.close() 
    f5 = open(Region_Path+'/'+'Step2_0Run_main'+(ftype)+'.sh',"w")
    corecount = 0
    fcount  = 0
    
    f5.write('#!/bin/bash')
    f5.write('\n')
    f5.write('chmod 700 *.sh')
    f5.write('\n')
    f5.write('module load nco')
    f5.write('\n')    
    f5.write('\n')
    testname = '*_split_'+(ftype)+'.nc'
    f6.write('count=$(find '+Region_Path+' -maxdepth 1 -name "*_split_h0.nc" | wc -l)')
    f6.write('\n')
    f6.write('while [ $count < '+str(splitcount)+' ]; do')
    f6.write('\n')
    f6.write('  echo "Automation is running......"')
    f6.write('\n')
    f6.write('  sleep 10s')
    f6.write('\n')
    f6.write('done')
    f6.write('\n')

    f6.write('./Step2_0Run_main'+ftype+'.sh')
    f6.write('\n')
    
    for filename in glob.iglob(f'{indir}*.cam.'+(ftype)+'.2008-10-*.nc'):
        SP_Case = filename[len(filename)-len(infile):len(filename)]
        coremax = corem
        Date_Time = SP_Case[len(SP_Case)-19:len(SP_Case)-3]
        
        f5.write('\n')
        f5.write('./'+'step2_runcombine-'+Date_Time+(ftype)+'.sh&')
        corecount = corecount + 1
        f5.write('\n')

        if corecount==coremax:
            f5.close() 
            fcount = fcount + 1
            f5 = open(Region_Path+'/Step2_'+str(fcount)+'Run_main'+(ftype)+'.sh',"w")
            f6.write('./Step2_'+str(fcount)+'Run_main'+(ftype)+'.sh')
            f6.write('\n')
            f5.write('#!/bin/bash')
            f5.write('\n')
            f5.write('chmod 700 *.sh')
            f5.write('\n')
            f5.write('module load nco')
            f5.write('\n')
            corecount = 0

    f6.write('cd ../')
    f6.write('\n')
    f6.write('mkdir '+rname)
    f6.write('\n')
    f6.write('cd '+rname)
    f6.write('\n')    
    f6.write('cp '+Region_Path+'/*mean*.nc .')    
    f5.close() 
    f6.close() 

    #f4.write('rm *'+rname+'_split_'+(ftype)+'.nc')
    #f4.write('\n')
    #f4.write('rm '+'*run_split-'+Date_Time+(ftype)+'.sh')
    #f4.write('\n')
    #f4.write('rm '+'step*.sh')    


if __name__ == '__main__':
    p  = argparse.ArgumentParser()
    p.add('-c', '--config_file',
                   is_config_file=True,
                   help='Name of config file.')
    p.add_argument('--in_dir',
                   default=None,
                   type=str,
                   help='Model history file path')

    p.add_argument('--in_filesample',
                   type=str,
                   default=None,
                   help='Sample model history file name')

    p.add_argument('--lon_lowleft',
                   type=float,
                   default=1.,
                   help='Longitude at the lower left corner '
                        'Default = 1.')

    p.add_argument('--lat_lowleft',
                   type=float,
                   default=1.,
                   help='Latitude at the lower left corner '
                        'Default = 1.')

    p.add_argument('--lon_upright',
                   type=float,
                   default=1.,
                   help='Longitude at the upper right corner '
                        'Default = 1.')

    p.add_argument('--lat_upright',
                   type=float,
                   default=1.,
                   help='Latitude at the upper right corner '
                        'Default = 1.')

    p.add_argument('--Region_Name',
                   type=str,
                   default=None,
                   help='This is the name of selected region')

    p.add_argument('--core_max',
                   type=int,
                   default=50,
                   help='Maximum number of tasks')

    p.add_argument('--cross360',
                   type=int,
                   default=0,
                   help='Flag used to identify lon range across 360')

    p.add_argument('--in_filetype',
                   type=str,
                   default=None,
                   help='Either h0 or h1')

    args = p.parse_args()
    preprocess(args)

