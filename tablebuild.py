import numpy as np
import os
from astroquery.simbad import Simbad
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord


starlist= open('binarylist.txt','r')
df= pd.read_fwf('binarylist.txt', names= ['Binary'])
starid=[]
starra=[]
stardec=[]

for binary in starlist:
    binary = binary.strip()
    #idtable= Simbad.query_objectids(binary)
    paramtable= Simbad.query_object(binary)
    pdparam= paramtable.to_pandas() #convert to Pandas table
    print(pdparam)
    pdparamfix= SkyCoord(pdparam['RA'], pdparam['DEC'], frame='icrs', unit='deg')
    print(pdparamfix)
    starra.append(pdparam['RA'][0])
    
    stardec.append(pdparam['DEC'][0])
    #idsearch=[x for x in idtable['ID'] if 'Gaia DR2' in x]
    #if len(idsearch) == 0:
    #    print(f"Gaia ID not found for {binary}")
    #    starid.append('--')
    #else:
    #    idstrip= [words.replace('Gaia DR2', '') for words in idsearch]      
    #    starid.append(idstrip[0])


#df['G2ID'] = pd.Series(starid)
df['RA']   = pd.Series(starra) 
df['DEC']  = pd.Series(stardec) 

print(df)
df.to_csv('binarytable.txt')

