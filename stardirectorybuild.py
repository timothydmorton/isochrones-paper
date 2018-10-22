import numpy as np
import os
from astroquery.simbad import Simbad
from astroquery.gaia import Gaia

starlist= open('binarylist.txt','r')

for binary in starlist:
    binary = binary.strip()
    paramtable= Simbad.query_objectids(binary)
    idsearch=[x for x in paramtable['ID'] if 'Gaia DR2' in x]
    if len(idsearch) == 0:
        print (f"Gaia ID not found for {binary}")
    else:
        idstrip= [words.replace('Gaia DR2', '') for words in idsearch]     
        job= Gaia.launch_job("SELECT \
        parallax, parallax_error, phot_g_mean_mag \
        FROM gaiadr2.gaia_source \
        Where source_id= %s" % idstrip[0])
        results= job.get_results()
        par = results['parallax'][0]
        epar = results['parallax_error'][0]
        mag = results['phot_g_mean_mag'][0]
        binary = binary.replace(" ", "_")
        os.makedirs(binary, exist_ok=True) 
        f= open(f'{binary}/star.ini', 'w+')
        line1= f"parallax = {par}\n"
        line2 = f"parallax_error = {epar}\n"
        line3 = f"mag = {mag}"
        isofile = line1, line2, line3
        f.writelines(isofile)
        f.close
        
