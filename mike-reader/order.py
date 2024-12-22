import numpy as np

class Order:
    '''
    -----------
    Parameters:
    
    order_str: String that contains all the data of every single order.
    -----------
    Attributes:
    
    order_number: float that represents the order number.
    active_flag: saves active_flag number.
    coord_type: saves coord type.
    start_wavelength: saves start wavelength in angstrom.
    dispersion: saves dispersion value.
    shift: saves shift value.
    range_start: saves range start.
    range_end: save range end.
    wavelengths: saves the calculated wavelengths.
    data: data directly from the fits file associated with the order.
    '''
    def __init__(self, order_str: str, data):
        self.order_str = order_str
        self.data = data
        self.order_number = None
        self.active_flag = None
        self.coord_type = None
        self.start_wavelength = None
        self.dispersion = None
        self.num_pixels = None
        self.shift = None
        self.range_start = None
        self.range_end = None
        self.wavelengths = None
        self.process()
        self.calc_wavelength()

    def process(self):

        self.order_str = self.order_str.split()

        self.order_number = self.order_str[0]
        #self.active_flag = self.order_str[3]
        #self.coord_type = self.order_str[4]
        self.start_wavelength = float(self.order_str[5])
        self.dispersion = float(self.order_str[6])
        self.num_pixels = float(self.order_str[7])
        #self.shift = self.order_str[4]
        #self.range_start = self.order_str[9]
        #self.range_end = self.order_str[10]

    def calc_wavelength(self):
        self.wavelengths = self.start_wavelength + np.arange(2048) * self.dispersion

    def __repr__(self):
        return f'order: {self.order_number}'
        #\nnum_pixel: {self.num_pixels}\ndispersion: {self.dispersion}\nstart wavelength: {self.start_wavelength}'