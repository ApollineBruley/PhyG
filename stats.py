import os,sys
import numpy as np

def resume_statistics(dir_results):
    operation_type=['Inversions', 'Translocations', 'Duplications', 'Deletions', 'Fusions', 'Fissions', 'WGD']
    compteur=np.zeros(10,7) # [simulation][Inversions, Translocations, Duplications, Deletions, Fusions, Fissions, WGD]
    nb_simu=0	
    for dir_res in os.listdir(dir_results):
        	fichier = dir_results+"/"+dir_res+"/statistics"
        	compteur=read_statistics(fichier,compteur, nb_simu)
        	nb_simu=nb_simu+1
    result= global_statistics(compteur)
    total={}
    for x in operation_type:
     for y in result:
        total[x] = y
    print(total)
    return 


def read_statistics(fichier_stat, dico_stat, nb_simu): # lit 1 fichier result
    alllines = fichier_stat.readlines()
    for line in alllines:
        print(line)
        if line[0:10] == 'Inversions':
            dico_stat[nb_simu][0]=int(line[16:19].strip())
        elif line[0:14] =='Translocations':
            dico_stat[nb_simu][1]=int(line[16:19].strip())
        elif line[0:13] =='Duplications':
            dico_stat[nb_simu][2]=int(line[16:19].strip())
        elif line[0:9] =='Deletions':
            dico_stat[nb_simu][3]=int(line[16:19].strip())
        elif line[0:7] =='Fusions':
            dico_stat[nb_simu][4]=int(line[16:19].strip())
        elif line[0:8] =='Fissions':
            dico_stat[nb_simu][5]=int(line[16:19].strip())
        elif line[0:8] =='WGD':
            dico_stat[nb_simu][6]=int(line[16:19].strip())
    return dico_stat



def global_statistics(res): # moyennes ou proportions
    l=np.zeros(7)
    size=res.shape
    for i in range(len(size[0])):
        for j in range(len(size[1])):
            l[j]=l[j]+res[i][j]
    return l

try:
	dir_results = sys.argv[1]
	statistics = resume_statistics(dir_results)
except:
	print("Veuillez entrer le nom du repertoire contenant les fichiers statistics en argument.")
