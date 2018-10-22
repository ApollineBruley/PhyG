import os

def resume_statistics(dir_results):
	statistiques={} # Dictionnaire qui somme les occurences de chaque evenement, pour nous faciliter a fiare la moyenne
	for dir_res in os.listdir(dir_results):
		fichier = dir_results+"/"+dir_res+"/statistics"
		read_statistics(fichier,statistiques)
	return statistics


def read_statistics(fichier_stat,dico_stat): # lit 1 fichier result
	return None # Retourne moyennes ou proportions
	


def write_statistics(): # moyennes ou proportions
	# Les ecrit dans un fichier
	return None