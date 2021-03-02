#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################
import os

def read_record(name,filename):
    with open (filename,"r") as file:
        strv = file.read()
    strv = strv.split("\n")

    for i in strv:
        if i.startswith(name):
            i = i.split(": ")
            if i[0]==(name):
                return i[1]

def read_list(filename):
    with open (filename,"r") as file:
        strv = file.read()
    strv = strv.split("\n")
    return strv

def write_record(name, value, filename):
    with open (filename,'r') as file:
        all = file.read()
    record = read_record(name, filename)
    os.remove(filename)
    if record is not None:
        all = all.replace("\n"+name + ": " + record, "")
    with open(filename,'w') as file:
        file.write(all + "\n" + name + ": " + value)