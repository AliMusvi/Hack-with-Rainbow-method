import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    passwordlist = OrderedDict()
    for this_one in range(1000,10000):
        hashpass = hashlib.sha256(str(this_one).encode()).hexdigest()
        passwordlist[str(hashpass)] = this_one

    unhasspass = OrderedDict()
    with open(input_file_name) as fin:
        reader = csv.reader(fin)

        for this_one in reader:               
            unhasspass.update({this_one[0] : passwordlist.get(this_one[1])})
        
        fin.close()

    with open(output_file_name, 'w', newline='') as fout:
        writer = csv.writer(fout)

        for this_one in unhasspass.items():
            writer.writerow(this_one)

        fout.close()