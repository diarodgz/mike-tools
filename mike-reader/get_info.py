from astropy.io import fits
from clean_data import clean_data_line

def read(path):

    '''
    ------------
    Parameters:

    path: string of the fits path.
    ------------
    Returns:

    orders: List that contains the string that corresponds to each order.
    data: An array that contains the entire data of the fits file. Every dimension of data.
    hdu: The hdu of the fits file.
    ------------
    '''

    open_fits = fits.open(path)
    hdu = open_fits[0].header
    data = open_fits[0].data
        
    order_str = ""
    for key in hdu.keys():
        # Saving all of the info of each order of the spectrum
        if 'WAT' in key:
            order_str += str(hdu[key])

    cleaned_orders = []
    orders = order_str.split('spec')[4:]

    for od in orders:
        c = clean_data_line(od)
        cleaned_orders.append(c)

    return cleaned_orders, data, hdu