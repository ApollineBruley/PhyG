import os,sys
import numpy as np

def resume_statistics(dir_results):
	statistiques=np.zeros(10,7) # Tableau [evenement][type : Inversions, Translocations, Duplications, Deletions, Fusions, Fissions, WGD]
	#On parcourt les fichiers results
	numero_simu=0
	for dir_res in os.listdir(dir_results):
		fichier = dir_results+"/"+dir_res+"/statistics"
		read_statistics(fichier,statistiques[numero_simu])
		numero_simu+=1
	return statistics


def read_statistics(fichier_stat,dico_stat): # lit 1 fichier result
	alllines = fichier_stat.readlines()
	i=0
	for line in alllines:
        	if line[1:11] == 'Inversions':
			dico_stat[i]=int(line[17:19])
	return None # Retourne moyennes ou proportions


def write_statistics(): # moyennes ou proportions
	# Les ecrit dans un fichier
	return None

try:
	dir_results = sys.argv[1]
	statistics = resume_statistics(dir_results)
except:
	print("Veuillez entrer le nom du repertoire contenant les fichiers statistics en argument.")
