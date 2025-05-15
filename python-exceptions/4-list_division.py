def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Vérifie si les deux éléments sont des nombres
            if not (isinstance(my_list_1[i], (int, float)) and 
                    isinstance(my_list_2[i], (int, float))):
                print("wrong type")
                result.append(0)
                continue
                
            # Tente la division
            try:
                division = my_list_1[i] / my_list_2[i]
                result.append(division)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
                
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
            
    return result
