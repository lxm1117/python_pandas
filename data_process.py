#! /usr/bin/env python

import pandas as pd
import matplotlib.pylab as plt
import numpy as np

def readData(dir):
	species0=pd.read_table("species_name_py.txt", header=None)
	species=species0[0]
	s=pd.Series(["time", "ca", "cam", "camca1", "camca2", "camca3", "cam_nano", "b2_nano", "g3_nano", "pump", "ca_pump"])
	names=pd.concat([s,species], ignore_index=True)

	observs=pd.read_table("observes_py.txt", header=None, sep=" ")
	bB0=[];bB1=[];bB2=[];bB3=[];bB4=[];bB5=[];bB6=[];
	gB0=[];gB1=[];gB2=[];gB3=[];gB4=[];gB5=[];gB6=[];
	for i in observs[2][0].split(','): bB0.append(int(i)+len(names)-len(species))
	for i in observs[2][1].split(','): bB1.append(int(i)+len(names)-len(species))
	for i in observs[2][2].split(','): bB2.append(int(i)+len(names)-len(species))
	for i in observs[2][3].split(','): bB3.append(int(i)+len(names)-len(species))
	for i in observs[2][4].split(','): bB4.append(int(i)+len(names)-len(species))
	for i in observs[2][5].split(','): bB5.append(int(i)+len(names)-len(species))
	for i in observs[2][6].split(','): bB6.append(int(i)+len(names)-len(species))

	for i in observs[2][14].split(','): gB0.append(int(i)+len(names)-len(species))
	for i in observs[2][15].split(','): gB1.append(int(i)+len(names)-len(species))
	for i in observs[2][16].split(','): gB2.append(int(i)+len(names)-len(species))
	for i in observs[2][17].split(','): gB3.append(int(i)+len(names)-len(species))
	for i in observs[2][18].split(','): gB4.append(int(i)+len(names)-len(species))
	for i in observs[2][19].split(','): gB5.append(int(i)+len(names)-len(species))
	for i in observs[2][20].split(','): gB6.append(int(i)+len(names)-len(species))


	file=dir+"nano.txt"
	data_nano=pd.read_table(file, header=None, sep=" ")
	data_nano.columns=names
	#data_nano_str=pd.read_table(file, header=None)
	#data_nano_s=data_nano_str[0]

	file=dir+"cytol.txt"
	data_cytol=pd.read_table(file, header=None, sep=" ")
	data_cytol.columns=names

	file=dir+"nucleus.txt"
	data_nucleus=pd.read_table(file, header=None, sep=" ")
	data_nucleus.columns=names

	file=dir+"membrane.txt"
	data_membrane=pd.read_table(file, header=None, sep=" ")
	data_membrane.columns=names

	file=dir+"sub_membrane.txt"
	data_membrane=pd.read_table(file, header=None, sep=" ")
	data_membrane.columns=names

	return True

