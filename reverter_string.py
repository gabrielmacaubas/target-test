def inverter_string(string):
    string_invertida = ""

    for i in range(-1, -(len(string)+1),-1):
        string_invertida += string[i]
    
    return string_invertida


print(inverter_string("ola mundo"))
