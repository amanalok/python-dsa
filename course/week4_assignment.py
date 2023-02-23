'''
*** PROBLEM 1 ***
'''

def _find_average(l):
    num_days = len(l)
    sum_rain = 0
    for rain in l:
        sum_rain += rain

    avg_rain = sum_rain / num_days
    return avg_rain

def rainaverage(l):
    avg_dict = {}
    
    for item in l:
        if item[0] in avg_dict:
            avg_dict[item[0]].append(item[1])
        else:
            avg_dict[item[0]] = [item[1]]

    avg_list = []
    for place, rain in avg_dict.items():
        avg_rain = _find_average(rain)
        avg_list.append((place, avg_rain))

    return avg_list


'''
*** PROBLEM 2 ***
'''

def _flatten(l, flattened_list, counter):

    if counter > len(l):
        return

    for item in l:
        if not type(item) is list:
            flattened_list.append(item)
            counter += 1
        elif type(item) is list and len(item) == 1:
            flattened_list.append(item[0])
            counter += 1
        elif type(item) is list:
            if counter < len(l):
                _flatten(l[counter:], flattened_list, len(l[counter:]))
                counter += 1
            else:
                _flatten(item, flattened_list, 0)
                
                if counter == len(l):
                    break
                
                counter += 1
                _flatten(l[counter:], flattened_list, counter)
                counter += 1
        else:
            raise Exception("Sorry, invalid input type")


def flatten(l):
    counter = 0
    flattened_list = []
    _flatten(l, flattened_list, counter)
    return flattened_list
