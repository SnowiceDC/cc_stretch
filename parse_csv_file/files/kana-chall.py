#!/usr/bin/python

hosts = open('../example.csv', 'r').readlines()
for hostname in hosts:
	linhas = hostname.split(',')

	host = linhas[0]+".yml"
	ip = linhas[1]
	interface = linhas[2]
	neighbor = linhas[3]

	with open(host, 'a') as novo_arquivo:
		novo_arquivo.write("- {} interface=\"{}\"\n ip=\"{}\"\n".format(neighbor,interface,ip))
