"""Functions to convert temperature between kelvin, celsius, and fahrenheit."""

author = 'Rick Forest'
    
def kelvins_to_celsius(temp_k):
    temp_c = temp_k - 273.15
    return temp_c

def celsius_to_fahr(temp_c):
    temp_f = (temp_c * 1.8) + 32
    return temp_f

def fahr_to_celsius(temp_f):
    temp_c = (temp_f - 32) / 1.8
    return temp_c

def celsius_to_kelvins(temp_c):
    temp_k = temp_c + 273.15
    return temp_k

def kelvins_to_fahr(temp_k):
    temp_f = celsius_to_fahr(kelvins_to_celsius(temp_k))
    return temp_f

def fahr_to_kelvins(temp_f):
    temp_k = celsius_to_kelvins(fahr_to_celsius(temp_f))
    return temp_k


def temp_converter(temp, convert_from = "c", convert_to = "f"):
    '''
    Function for converting temperature from one scale to another.

    Parameters
    ----------
    temp: <numerical>
        Temperature 
    convert_from: <str>
        Input temperature scale. Supported values: 'c' | 'f' | 'k'
    convert_to: <str>
        Output temperature scale. Supported values: 'c' | 'f' | 'k'

    Returns
    -------
    Converted temperature <float>.
    
    '''

    convert_from = convert_from.lower()
    convert_to = convert_to.lower()

    
    if convert_from not in ['c','f','k']:
            print('convert_from must be c, f, or k')
            return
    if convert_to not in ['c','f','k']:
            print('convert_to must be c, f, or k')
            return
        
    if convert_from == "k":
        if convert_to == "c":
            converted_temp = kelvins_to_celsius(temp)
        elif convert_to == "f":
            converted_temp = kelvins_to_fahr(temp)
            
    elif convert_from == "c":
        if convert_to == "k":
            converted_temp = celsius_to_kelvins(temp)
        elif convert_to == "f":
            #converted_temp = (temp * 1.8) + 32
            converted_temp = celsius_to_fahr(temp)
            
    elif convert_from == "f":
        if convert_to == "k":
            converted_temp = fahr_to_kelvins(temp)
        elif convert_to == "c":
            converted_temp = fahr_to_celsius(temp)
                 
    print(f'from: {temp} {convert_from} to: {convert_to} {converted_temp}')

    # Return the result
    return converted_temp