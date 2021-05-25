#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ln_trans(var):
    """ Natural log transform a variable and create a new variable in pandas dataset

    Parameters
    ----------
    var : int or float
        Numeric value to transform
    

    Returns
    -------
    ln : int or flow
        Numeric value natural log transformed

    """
    ln = np.log(var)

    return ln

