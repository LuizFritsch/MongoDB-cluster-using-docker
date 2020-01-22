# Passo a passo de como criar containers mongo (master-slave) no linux:<br>

* Você deve executar com permissões de root

1.Crie uma rede docker
```console
WhoAmI@WhoAmI:~$ docker network create my-mongo-cluster  
```

2.Liste as redes criadas  
```console
WhoAmI@WhoAmI:~$ docker network ls  
```

3.Execute e crie os containers setando o nome, a rede utilizada, a aplicacao mongo   
```console
WhoAmI@WhoAmI:~$ docker run -p 30500:27017 --name container1 --net my-mongo-cluster mongo mongod --replSet my-mongo-set  
WhoAmI@WhoAmI:~$ docker run -p 30501:27017 --name container2 --net my-mongo-cluster mongo mongod --replSet my-mongo-set  
WhoAmI@WhoAmI:~$ docker run -p 30502:27017 --name container3 --net my-mongo-cluster mongo mongod --replSet my-mongo-set
```

4.Aqui configure o container1 como mestre, e os dois restantes como escravos na porta 27017, padrao do mongo
```console
WhoAmI@WhoAmI:~$ config={"_id":"my-mongo-set","members":[{"_id":0,"host":"container1:27017"},{"_id":1,"host":"container2:27017"},{"_id":2,"host":"container3:27017"}]}  
```
5.inicialize a configuracao definida 
```console
WhoAmI@WhoAmI:~$ rs.initiate(config)  
```
6.mapear a porta 27017 pra que possa acessar a mesma dentro do container  
```console
WhoAmI@WhoAmI:~$ docker run -d -p 27017:27017 mongo  
```
# passo a passo de como executar:  

1.Primeiramente você deve executar seus containers  
```console
WhoAmI@WhoAmI:~$ docker start container1 container2 container3  
```
2.Agora abra 3(três) terminais e em cada um executa 1(um) container no modo iterativo   
```console
WhoAmI@WhoAmI:~$ docker exec -it container1 mongo  
WhoAmI@WhoAmI:~$ docker exec -it container2 mongo  
WhoAmI@WhoAmI:~$ docker exec -it container3 mongo  
```
Deve aparecer algo como:      
```console
my-mongo-set:PRIMARY>  
my-mongo-set:SECONDARY>  
``` 
3.Em cada um dos terminais respectivamente você deve inicializar com 
```python
db = (new Mongo('container1:27017')).getDB('test')  
db = (new Mongo('container2:27017')).getDB('test')  
db = (new Mongo('container3:27017')).getDB('test')  
```
4.Agora você deve setar o container2 e o container3 como escravos(slave)
```python
db.setSlaveOk()  
```
5.Pronto! divirta-se! 

-Exemplos de operações com o mongo:  
```python
db.Personagens.insert({"nome":'captain america',"raca":'human',"classe":'warrior',"vida":97})  
db.Personagens.find()  
db.Personagens.find().pretty()  
db.Personagens.find().count()  
db.Personagens.remove({})  
``` 


*Se você deseja usar seu cluster de fora dos containers, utilize o pymongo. no arquivo geraCargaMongoDB.py, tem exemplos claros de como utilizar!  


<hr>


# Step by step of how to create mongo master-slave containers on linux:<br>
1.Create a docker network
```console
WhoAmI@WhoAmI:~$ docker network create my-mongo-cluster  
```

2.List all the docker networks  
```console
WhoAmI@WhoAmI:~$ docker network ls  
```

3.Execute and create three docker containers setting their names, their network and their image(mongodb)  
```console
WhoAmI@WhoAmI:~$ docker run -p 30500:27017 --name container1 --net my-mongo-cluster mongo mongod --replSet my-mongo-set  
WhoAmI@WhoAmI:~$ docker run -p 30501:27017 --name container2 --net my-mongo-cluster mongo mongod --replSet my-mongo-set  
WhoAmI@WhoAmI:~$ docker run -p 30502:27017 --name container3 --net my-mongo-cluster mongo mongod --replSet my-mongo-set
```

4.Configure container1 as master, the container2 and 3 as slaves on port 27017.
```console
WhoAmI@WhoAmI:~$ config={"_id":"my-mongo-set","members":[{"_id":0,"host":"container1:27017"},{"_id":1,"host":"container2:27017"},{"_id":2,"host":"container3:27017"}]}  
```

5.initialize config  
```console
WhoAmI@WhoAmI:~$ rs.initiate(config)  
```

6.map port 27017 so you can acces inside the container  
```console
WhoAmI@WhoAmI:~$ docker run -d -p 27017:27017 mongo  
```

# How to execute your mongo cluster:

1.First of all you must run all the containers  
```console
WhoAmI@WhoAmI:~$ docker start container1 container2 container3  
```

2.Now open 3(three) terminals and in each one execute 1(one) container on iterative mode  
```console
WhoAmI@WhoAmI:~$ docker exec -it container1 mongo  
WhoAmI@WhoAmI:~$ docker exec -it container2 mongo  
WhoAmI@WhoAmI:~$ docker exec -it container3 mongo  
```

terminal should looks like this:     
```console
my-mongo-set:PRIMARY>  
my-mongo-set:SECONDARY>  
``` 

3.On each terminal you should respectively initialize with
```python
db = (new Mongo('container1:27017')).getDB('test')  
db = (new Mongo('container2:27017')).getDB('test')  
db = (new Mongo('container3:27017')).getDB('test')  
```

4.Now you must set container2 and container3 as slaves
```python
db.setSlaveOk()  
```

5.Now it is ready! Have fun!  


-Examples of operations on mongo:
```python
db.Personagens.insert({"nome":'captain america',"raca":'human',"classe":'warrior',"vida":97})  
db.Personagens.find()  
db.Personagens.find().pretty()  
db.Personagens.find().count()  
db.Personagens.remove({})  
``` 

*If you want to use your cluster from outside it, you should use pymongo. The file geraCargaMongoDB.py has clear examples of how to use it!   
