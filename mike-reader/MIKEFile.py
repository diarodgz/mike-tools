from order import Order
from get_info import read

class MIKEFile:
    '''
    ----------
    Parameters:

    path: str of the fits file path.
    ----------
    Attributes:

    order = list of all of the order objects
    ----------
    Methods:

    '''
    def __init__(self, path: str):
        self.path = path
        self.order = None
        self.hdu = None
        self.open_data()

    def open_data(self):
        
        # Open fits, get order string and data.
        orders, data, hdu = read(self.path)
        self.hdu = hdu
        # Send list of orders and data to create an Order object for them.
        self.access_orders(orders, data)

        
    def access_orders(self, orders, data):
        all_orders = [] #list(map(lambda ord, d: Order(ord, d), orders, data))

        for order in orders:
            o = Order(order, data[6])
            all_orders.append(o)
            #print(f'Adding data {data[6]}...')

        self.order = all_orders

    def __str__(self):
        return self.path

    def __repr__(self) -> str:
        return self.path