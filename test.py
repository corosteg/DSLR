import sys
import pandas as pd

def open_and_read_file(argv):
    if len(argv) != 2:
        print("describe:")
        print("Usage: describe <dataset_train.csv>")
        sys.exit(1)

    try:
        fd = open(argv[1], "r")
    except:
        print("Describe a file with read permission in argument")
        sys.exit(1)

    return fd.read()

def find_average(arr):
    arr_sum = 0

    for value in arr:
        arr_sum = arr_sum + value

    return arr_sum / len(arr)

def find_std(arr):
    deviation = 0
    average = find_average(arr)

    for value in arr:
        deviation = deviation + ((value **2) - (average ** 2))

    deviation = deviation / (len(arr) - 1)

    deviation = deviation ** 0.5

    # print(deviation)
    return deviation

def find_min(arr):
    min_val = arr[0]

    for value in arr:
        if (value < min_val):
            min_val = value
    return min_val

def find_max(arr):
    max_val = arr[0]

    for value in arr:
        if (value > max_val):
            max_val = value
    return max_val

if __name__ == "__main__":
    features = []
    data = open_and_read_file(sys.argv)
    features_names = []
    feature = {}
    count = {}
    std = {}
    mean = {}
    min_val = {}
    max_val = {}

    pand = pd.read_csv('./test.csv')
    print(pand.describe(), '\n')
    
    lst_data = data.split('\n')

    for value in lst_data:
        features.append(value.split(','))
    
    features_names = features[0]

    for value in features_names:
        feature[value] = []

    features.pop(0)
    features.pop(len(features) - 1)

    for index in range(len(features)):
        for i in range(len(features[index])):
            if (features[index][i] != ''):
                try:
                    try:
                        features[index][i] = int(features[index][i])
                        feature[features_names[i]].append(features[index][i])
                    except:
                        features[index][i] = float(features[index][i])
                        feature[features_names[i]].append(features[index][i])
                except:
                    pass

    new_features_names = []
    for value in features_names:
        if (len(feature[value]) != 0):
            new_features_names.append(value)

    for value in new_features_names:
        count[value] = len(feature[value])
        std[value] = round(find_std(feature[value]), 6)
        mean[value] = round(find_average(feature[value]), 6)
        min_val[value] = round(find_min(feature[value]), 6)
        max_val[value] = round(find_max(feature[value]), 6)

    print(min_val)
    print(max_val)
