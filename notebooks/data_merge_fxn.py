#!/usr/bin/env python
# coding: utf-8

# # Functions to process and merge GRanD and FFR data

# In[ ]:


# Import needed for functions to run
import os


# In[ ]:


# FUNCTIONS TO PROCESS GRanD dam 'MAIN_USE' INTO NEW VARIABLES
# CREATE REVSIED MAIN_USE CLASS THAT GROUPS DAMS WITH SIMILAR HYDROLOGIC EFFECTS
def reduce_dam(grand_proc, new_class):
    """ Creates a collapsed main use category that lumps dams
    listed as Recreation, Fisheries, and Other into a generic "Other expanded"
    class. 
    
    Parameters
    -----------
    grand_proc : geodataframe
        Processed geodataframe to add new column
        
    new_class : string
        Name of new dam main use column to be created
    
    Returns
    --------
    grand_proc :geodataframe
        The geodataframe with the added newly created column
    """
    grand_proc[new_class]=grand_proc['MAIN_USE']
    grand_proc.loc[(grand_proc['MAIN_USE'] == 'Recreation') |
                         (grand_proc['MAIN_USE'] == 'Fisheries') |
                         (grand_proc['MAIN_USE'] == 'Other'), 'MAIN_RED'] = 'Other expanded'
    
    return grand_proc


# CREATE EXPANDED HYDRO-ELECTRIC CLASSES
def reclass_dam(grand_proc, new_class):
    """ Creates an expanded dam main use category that indicates whether a dam
    is listed as having hydroelectric usage but may have a different main
    purpose listed. This function creates new classes that combine the
    main use and secondary hydroelectric use dam category as new labels.
    
    Parameters
    -----------
    grand_proc : geodataframe
        Processed geodataframe to add new column
        
    new_class : string
        Name of new dam main use column to be created
    
    Returns
    --------
    grand_proc :geodataframe
        The geodataframe with the added newly created column
    """
    grand_proc[new_class]=grand_proc['MAIN_RED']
    grand_proc.loc[(grand_proc['USE_ELEC'] =='Major') |
                        (grand_proc['USE_ELEC'] =='Sec')  & 
                        (grand_proc['MAIN_RED'] == 'Irrigation'), new_class] = 'Hydro_irrig'

    grand_proc.loc[(grand_proc['USE_ELEC'] =='Major') |
                        (grand_proc['USE_ELEC'] =='Sec')  & 
                        (grand_proc['MAIN_RED'] == 'Water supply'), new_class] = 'Hydro_water'

    grand_proc.loc[(grand_proc['USE_ELEC'] =='Major') |
                        (grand_proc['USE_ELEC'] =='Sec')  & 
                        (grand_proc['MAIN_RED'] == 'Navigation'), new_class] = 'Hydro_navig'

    grand_proc.loc[(grand_proc['USE_ELEC'] =='Major') |
                        (grand_proc['USE_ELEC'] =='Sec')  & 
                        (grand_proc['MAIN_RED'] == 'Flood control'), new_class] = 'Hydro_flood'

    grand_proc.loc[(grand_proc['USE_ELEC'] =='Major') |
                        (grand_proc['USE_ELEC'] =='Sec')  & 
                        (grand_proc['MAIN_RED'] == 'Other_expanded'), new_class] = 'Hydro_other'
    
    return grand_proc


# CREATE VARIABLE TO INDICATE WHETHER HYDROELECTRIC IS LISTED FOR ANY USE
def reclass_hydro(grand_proc, new_class):
    """ Creates a simplified dam main use category that indicates whether hydroelectric
    is listed as a primary or secondary purpose for a dam and will refer to it simply as
    hydroelectric. 
    
    Parameters
    -----------
    grand_proc : geodataframe
        Processed geodataframe to add new column
    
    new_class : string
        Name of new dam main use column to be created
    
    Returns
    --------
    grand_proc :geodataframe
        The geodataframe with the added newly created column
    """
    grand_proc[new_class]=grand_proc['MAIN_HYDEXP']
    grand_proc.loc[(grand_proc['MAIN_HYDEXP']== 'Hydro_irrig')|
                (grand_proc['MAIN_HYDEXP']== 'Hydro_water')|
                (grand_proc['MAIN_HYDEXP']== 'Hydro_navig')|
                (grand_proc['MAIN_HYDEXP']== 'Hydro_flood')|
                (grand_proc['MAIN_HYDEXP']== 'Hydro_other')|
                (grand_proc['MAIN_HYDEXP']== 'Hydroelectricity'), new_class] = 'Hydroelectricity'
    
    return grand_proc


# CREATE DUMMY VARIABLE TO INDICATE WHETHER HYDROELECTRIC DAM OR NOT
def reclass_dummy(grand_proc, new_class):
    """ Creates a binary (T/F) dam main use category to indicate whether a dam is 
    used for hydroelectricity (main and/or secondary) or not. 
    '1' = hydroelectric; '0' = not hydroelectric
    
    Parameters
    -----------
    grand_proc : geodataframe
        Processed geodataframe to add new column
    
    new_class : string
        Name of new dam main use column to be created
    
    Returns
    --------
    grand_proc :geodataframe
        The geodataframe with the added newly created column
    """
    grand_proc[new_class] = grand_proc['MAIN_HYDRO'].apply(lambda x: '1' if (x=='Hydroelectricity')
                                                           else '0')    
    return grand_proc



# FUNCTION TO JOIN GRAND AND FFR DATA based on GOID

def grand_ffr_join(grand_dat,
                   ffr_dat):
    """ Merge Free-flowing rivers data subset with processed GRanD data and create
        new geodataframe of matching river segments and with dam observations based on GOID.
    
    Parameters
    -----------
    grand_dat : geodataframe
        Processed GRanD dam dataset with new columns and GOID added
    ffr_dat : geodataframe 
        Subset of free-flowing river data
    
    Returns
    ----------
    ffr_grand : geodataframe
        A geodataframe of matching FFR and GRanD observations that maintains the river geometry
    """

    grand_ffr = grand_dat.merge(ffr_dat, on="GOID", how="inner")
    
    return grand_ffr

