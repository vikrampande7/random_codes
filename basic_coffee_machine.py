syrup = {'vanilla':2, 'hazelnut':3, 'raspberry': 3}
espresso = {'one':1, 'two':2, 'three': 3}
milk = {'2p':2, '1p':2, 'hnh': 3, 'soy':3, 'almond': 3}


def get_price(s, e, m):
    return syrup.get(s) + espresso.get(e) + milk.get(m)


price = get_price('vanilla', 'one', 'almond')
print(f"The price of your coffee is: ${price}")
