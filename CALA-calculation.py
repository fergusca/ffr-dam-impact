#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def CA_LA(ca_area, lk_area):
    """ The ratio between catchment area and reservoir surface area associated with a dam.
    This metric is a proxy for the natural water residence time of a system based on
    the relative size of the watershed area draining into the receiving lake body
    
    Parameters
    ----------
    ca_area : int or float
            Numeric value of the catchment area
    
    lk_area : int or float
            Numeric value of the reservoir surface area
    
    
    Returns
    CALA : int or float
            Numeric value of the ratio between catchment area and reservoir surface area
    """
    CALA = ca_area/lk_area
    
    return CALA

