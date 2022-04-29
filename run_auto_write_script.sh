#!/bin/bash

# SP =============================================
# Namibian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/SP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_32_x_120z1200m.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample SP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_32_x_120z1200m.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -20.00 --lon_lowleft 350.00 --lat_upright 0.00 --lon_upright 360.00 --Region_Name Namibian --core_max 50 --cross360 1 --in_filetype h0

# Peruvian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/SP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_32_x_120z1200m.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample SP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_32_x_120z1200m.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -30.00 --lon_lowleft 265.00 --lat_upright -8.00 --lon_upright 290.00 --Region_Name Peruvian --core_max 50 --cross360 0 --in_filetype h0

# Australian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/SP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_32_x_120z1200m.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample SP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_32_x_120z1200m.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -39.00 --lon_lowleft 94.00 --lat_upright -20.00 --lon_upright 109.00 --Region_Name Australian --core_max 50 --cross360 0 --in_filetype h0

# UP =============================================

# Namibian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/UP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample UP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -20.00 --lon_lowleft 350.00 --lat_upright 0.00 --lon_upright 360.00 --Region_Name Namibian --core_max 50 --cross360 1 --in_filetype h0

# Peruvian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/UP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample UP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -30.00 --lon_lowleft 265.00 --lat_upright -8.00 --lon_upright 290.00 --Region_Name Peruvian --core_max 50 --cross360 0 --in_filetype h0

# Australian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/UP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample UP_newsst_long_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -39.00 --lon_lowleft 94.00 --lat_upright -20.00 --lon_upright 109.00 --Region_Name Australian --core_max 50 --cross360 0 --in_filetype h0


# UPhy =============================================

# Namibian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -20.00 --lon_lowleft 350.00 --lat_upright 0.00 --lon_upright 360.00 --Region_Name Namibian --core_max 50 --cross360 1 --in_filetype h0

# Peruvian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -30.00 --lon_lowleft 265.00 --lat_upright -8.00 --lon_upright 290.00 --Region_Name Peruvian --core_max 50 --cross360 0 --in_filetype h0

# Australian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -39.00 --lon_lowleft 94.00 --lat_upright -20.00 --lon_upright 109.00 --Region_Name Australian --core_max 50 --cross360 0 --in_filetype h0


# UPhysedi12 =============================================

# Namibian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_sedi12_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_sedi12_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -20.00 --lon_lowleft 350.00 --lat_upright 0.00 --lon_upright 360.00 --Region_Name Namibian --core_max 50 --cross360 1 --in_filetype h0

# Peruvian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_sedi12_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_sedi12_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -30.00 --lon_lowleft 265.00 --lat_upright -8.00 --lon_upright 290.00 --Region_Name Peruvian --core_max 50 --cross360 0 --in_filetype h0

# Australian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_sedi12_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_sedi12_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -39.00 --lon_lowleft 94.00 --lat_upright -20.00 --lon_upright 109.00 --Region_Name Australian --core_max 50 --cross360 0 --in_filetype h0


# UPhysedi15 =============================================

# Namibian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_sedi15_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_sedi15_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -20.00 --lon_lowleft 350.00 --lat_upright 0.00 --lon_upright 360.00 --Region_Name Namibian --core_max 50 --cross360 1 --in_filetype h0

# Peruvian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_sedi15_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_sedi15_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -30.00 --lon_lowleft 265.00 --lat_upright -8.00 --lon_upright 290.00 --Region_Name Peruvian --core_max 50 --cross360 0 --in_filetype h0

# Australian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_sedi15_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_sedi15_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -39.00 --lon_lowleft 94.00 --lat_upright -20.00 --lon_upright 109.00 --Region_Name Australian --core_max 50 --cross360 0 --in_filetype h0


# UPhysedi17 =============================================

# Namibian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_sedi17_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_sedi17_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -20.00 --lon_lowleft 350.00 --lat_upright 0.00 --lon_upright 360.00 --Region_Name Namibian --core_max 50 --cross360 1 --in_filetype h0

# Peruvian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_sedi17_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_sedi17_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -30.00 --lon_lowleft 265.00 --lat_upright -8.00 --lon_upright 290.00 --Region_Name Peruvian --core_max 50 --cross360 0 --in_filetype h0

# Australian
python3 Auto_Write_ProcessDataScript.py --in_dir /scratch1/07088/tg863871/HPhyper_sedi17_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera/run/ --in_filesample HPhyper_sedi17_long_newsst_L125_ERA5_2008_F-MMF1_frontera_ne16pg2_r05_oQU240_CRM1_64_x_120z200m.0.5s_crm_nx_rad_16_np_768_nlev_125.frontera.cam.h0.2008-10-13-29400.nc --lat_lowleft -39.00 --lon_lowleft 94.00 --lat_upright -20.00 --lon_upright 109.00 --Region_Name Australian --core_max 50 --cross360 0 --in_filetype h0
