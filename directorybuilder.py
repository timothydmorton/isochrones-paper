##Takes csv table of values and outputs a directory for each star filled with a star.ini file of its parameters

import numpy as np
import os
import pandas as pd


df = pd.read_csv('fullgaiacrossmatch-result.csv', keep_default_na=False)

for index, star in df.iterrows():
    name                 = star['binaryname']
    gaiaid               = star['source_id']
    ra                   = star['ra']
    ra_error             = star['ra_error']
    dec                  = star['dec']
    dec_error            = star['dec_error']
    parallax             = star['parallax']
    parallax_error       = star['parallax_error']
    
    phot_g_mean_mag      = star['phot_g_mean_mag']
    phot_flux_g          = star['phot_g_mean_flux']
    mg                   = 25.6884 - 2.5*np.log10( phot_flux_g )
    ephot_flux_g         = star['phot_g_mean_flux_error']
    emg                  = 25.6884 - 2.5*np.log10( ephot_flux_g )
    
    phot_bp_mean_mag     = star['phot_bp_mean_mag']
    phot_flux_bp         = star['phot_bp_mean_flux']
    mbp                  = 25.3514 - 2.5*np.log10( phot_flux_bp )
    ephot_flux_bp        = star['phot_bp_mean_flux_error']
    embp                 = 25.3514 - 2.5*np.log10( ephot_flux_bp )
    
    phot_rp_mean_mag     = star['phot_rp_mean_mag']
    phot_flux_rp         = star['phot_rp_mean_flux']
    mrp                  = 24.7619 - 2.5*np.log10( phot_flux_rp )
    ephot_flux_rp        = star['phot_rp_mean_flux_error']
    emrp                 = 24.7619 - 2.5*np.log10( ephot_flux_rp )
    
    j_m                  = star['j_m']
    j_msigcom            = star['j_msigcom']
    h_m                  = star['h_m']
    h_msigcom            = star['h_msigcom']
    ks_m                 = star['ks_m']
    ks_msigcom           = star['ks_msigcom']
    w1mpro               = star['w1mpro']
    w1mpro_error         = star['w1mpro_error'] 
    w2mpro               = star['w2mpro']
    w2mpro_error         = star['w2mpro_error']
    w3mpro               = star['w3mpro']
    w3mpro_error         = star['w3mpro_error']
    w4mpro               = star['w4mpro']
    w4mpro_error         = star['w4mpro_error']
    g_mean_psf_mag       = star['g_mean_psf_mag']
    g_mean_psf_mag_error = star['g_mean_psf_mag_error']
    r_mean_psf_mag       = star['r_mean_psf_mag']
    r_mean_psf_mag_error = star['r_mean_psf_mag_error']
    i_mean_psf_mag       = star['i_mean_psf_mag_error']
    i_mean_psf_mag_error = star['i_mean_psf_mag_error']
    z_mean_psf_mag       = star['z_mean_psf_mag']
    z_mean_psf_mag_error = star['z_mean_psf_mag_error']
    y_mean_psf_mag       = star['y_mean_psf_mag']
    y_mean_psf_mag_error = star['y_mean_psf_mag_error']
    os.makedirs(name, exist_ok=True)
    f= open(f'{name}/star.ini', 'w+')
    line0  = f"GaiaID = {gaiaid}\n" #gaiadr2
    line1  = f"parallax = {parallax}, {parallax_error}\n" #gaiadr2
    line2  = f"RA = {ra}, {ra_error}\n" #gaiadr2
    line3  = f"DEC = {dec}, {dec_error}\n" #gaiadr2
    line4  = f"G = {mg}, {emg}\n" #gaiadr2
    line5  = f"BP = {mbp}, {embp}\n" #gaiadr2
    line6  = f"RP = {mrp}, {emrp} \n" #gaiadr2 
    line7  = f"J = {j_m}, {j_msigcom} \n" #2mass
    line8  = f"H = {h_m}, {h_msigcom}\n" #2mass
    line9  = f"K = {ks_m}, {ks_msigcom}\n" #2mass
    line10  = f"W1 = {w1mpro}, {w1mpro_error}\n" #allwise
    line11 = f"W2 = {w2mpro}, {w2mpro_error}\n" #allwise
    line12 = f"W3 = {w3mpro}, {w3mpro_error}\n" #allwise
    line13 = f"W4 = {w4mpro}, {w4mpro_error}\n" #allwise
    line14 = f"g = {g_mean_psf_mag}, {g_mean_psf_mag_error}\n" #panstarrs
    line15 = f"r = {r_mean_psf_mag}, {r_mean_psf_mag_error}\n" #panstarrs
    line16 = f"i = {i_mean_psf_mag}, {i_mean_psf_mag_error}\n" #panstarrs
    line17 = f"z = {z_mean_psf_mag}, {z_mean_psf_mag_error}\n" #panstarrs
    line18 = f"y = {y_mean_psf_mag}, {y_mean_psf_mag_error}\n" #panstarrs
    isofile = line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17, line18
    for x in isofile:
        if ' , ' not in x:
            f.writelines(x)
 
    f.close
