

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
    print(indir)
    print(infile)
    print(lonll)
    print(latll)
    print(latur)
    print(lonur)
    print(rname)
    print(ftype)
    print(corem)
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

    ind_Peruvian = ind_Peruvian[1:]
    #print(ind_Peruvian)


    Region_Path = indir+rname+'_Run'
    cmd = 'mkdir '+ Region_Path
    os.system(cmd)
    f4 = open(Region_Path+'/'+'Run_main'+(ftype)+'.sh',"w")
    f4.write('#!/bin/bash')
    f4.write('\n')
    f4.write('chmod 700 *.sh')
    f4.write('\n')
    f4.write('module load nco')
    f4.write('\n')
    for filename in glob.iglob(f'{indir}*.cam.'+(ftype)+'.2008-10-*.nc'):
        print(filename)
        SP_Case = filename[len(filename)-len(infile):len(filename)]
        coremax = corem
        Date_Time = SP_Case[len(SP_Case)-19:len(SP_Case)-3]
        indexstr = (ind_Peruvian)
        
        fcount = 0
        corecount = 0
        f4.write('./'+'step1_runsplit-'+Date_Time+(ftype)+'.sh')
        f4.write('\n')
        f4.write('./'+'step2_runcombine-'+Date_Time+(ftype)+'.sh')
        f4.write('\n')
        f3 = open(Region_Path+'/'+'step2_runcombine-'+Date_Time+(ftype)+'.sh',"w")
        f3.write('#!/bin/bash')
        f3.write('\n')
        f3.write('ncra ')
        print('Liran check here')
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
            if corecount==coremax:

                f.write('echo $(date +%T)')
                f.write('\n')
                #f.write('wait')
                #f.write('\n')
                #f.write('echo $(date +%T)')

                f.close()
                fcount = fcount + 1
                #print(str(fcount)+'run_split-'+Date_Time+'.sh')
                f = open(Region_Path+'/'+str(fcount)+'run_split-'+Date_Time+(ftype)+'.sh',"w")
                f.write('#!/bin/bash')
                f.write('\n')
                f2.write('./'+str(fcount)+'run_split-'+Date_Time+(ftype)+'.sh')
                f2.write('\n')
                corecount = 0

            if corecount < coremax:
                #print(indexstr[il])
                SP_Case2 = SP_Case[0:len(SP_Case)-3]+'_'+str(indexstr[il])+'_'+rname+'_split_'+(ftype)+'.nc'
                f3.write(SP_Case2+' ')
                
                evalstring = 'ncea -F -d ncol,'+str(indexstr[il])+' ' +indir+ SP_Case+' '+Region_Path+'/'+SP_Case2 +' ' #& 
                f.write(evalstring)
                f.write('\n')
                corecount = corecount + 1

        #UPhy = eval(evalstring)
        f3.write(Date_Time+rname+'_mean_'+(ftype)+'.nc')
        f3.write('\n')
        #f3.write('rm *'+rname+'_split.nc')
        f3.write('\n')
        #f3.write('rm '+'*run_split-'+Date_Time+'.sh')
        
        f3.close() 
        f2.close()   
        f.close()
    f4.write('\n')
    f4.write('rm *'+rname+'_split_'+(ftype)+'.nc')
    f4.write('\n')
    f4.write('rm '+'*run_split-'+Date_Time+(ftype)+'.sh')
    f4.write('\n')
    f4.write('rm '+'step*.sh')    
    f4.close() 

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

