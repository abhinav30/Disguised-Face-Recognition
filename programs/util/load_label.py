def load_label(file_name):
    file  = open(file_name,"r")
    label_dict={}
    for line in file:
        values = line.split(':')
        label_dict[values[0]]=int(values[1])
    return label_dict



