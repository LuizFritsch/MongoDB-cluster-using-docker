import pymongo
from pymongo import MongoClient
import random as randint
import time
import thread
client = MongoClient('mongodb://localhost:30500/')
db = client['test']


nomes = ['gandalf','bilbo','frodo','arnaldo','galvao','lock','bulk','cafetao america','porco aranha']
racas = ['anao','elfo','humano','orc']
classes = ['mago','arcanista','feiticeiro','elementalista','ilusionista','druid','metamorfo','necromante','bardo','paladino'] 

size = 100000
inicio = time.time()
for x in range(0,size):
	db.Personagens.insert({"nome":randint.choice(nomes),"raca":randint.choice(racas),"classe":randint.choice(classes),"vida":randint.randint(0,100)})
fim = time.time()

insere = fim - inicio
qtdReg = db.Personagens.count()

inicioL = time.time()
db.Personagens.find();
fimL = time.time()

le = fimL - inicioL
arquivo = open('DadosMongo.txt', 'w')
texto =[]
texto.append('0000000##################################################\n')
texto.append('Tempo pra inserir'+str(size)+' de documentos: '+str(insere)+'\n')
texto.append('##################################################\n')
texto.append('\n')	
texto.append('\n')
texto.append('\n')
texto.append('Qtd reg banco:'+str(qtdReg)+'\n')	
texto.append('\n')
texto.append('\n')
texto.append('\n')
texto.append('##################################################\n')
texto.append('Tempo de leitura de '+str(qtdReg)+': '+str(le)+'\n')
texto.append('##################################################\n')
texto.append('Nmr de bulks magos: '+str(db.Personagens.find({"nome":'bulk',"classe":'mago'}).count()))
texto.append('\n##################################################\n')
texto.append('Nmr de bilbos druidas anoes: '+str(db.Personagens.find({"nome":'bilbo',"classe":'druid',"raca":'anao'}).count()))
texto.append('\n##################################################\n')





#Pega todos personagens que tem vida entre 95 e 99
#br.Personagens.find({"vida":{$gt:95,$lt:99}}).count()



#Atualiza todos com nome igual para o nome correto
#inicioLsa = time.time()
#db.Personagens.updateMany({"nome":'cafetao america'},{$set:{"nome":'capitao america'}})
#fimLsa = time.time()
#texto.append("\n\ntempo para de execucao para modificar "+str(db.Personagens.find({"nome":'cafetao america'}).count())+" :" str(fimLsa-inicioLsa))


#Localiza todos que tem um nome com a palavra 'capitao'
#db.Personagens.find({"nome":{$regex:'.*capitao.*'}})

#Remover todos 'galvao' do banco
#db.Personagens.remove({"nome":'galvao'})


arquivo.writelines(texto)
