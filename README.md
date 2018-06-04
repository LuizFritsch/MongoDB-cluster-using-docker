# mongodb-docker-master-slave
Trabalho de redes

# //Passo a passo de como criar containers mongo (master-slave) no linux:<br>
# //Step by step of how to create mongo master-slave containers on linux:<br>
<p>
//crie uma rede docker..
//create a docker network..
$docker network create my-mongo-cluster..</p>

<p>
//liste as redes criadas
//list all the docker networks
$docker network ls</p>


//execute e crie os containers setando o nome, a rede utilizada, a aplicacao mongo
//execute and create three docker containers setting their names, their network and their image(mongodb)
$docker run -p 30500:27017 --name container1 --net my-mongo-cluster mongo mongod --replSet my-mongo-set
$docker run -p 30501:27017 --name container2 --net my-mongo-cluster mongo mongod --replSet my-mongo-set
$docker run -p 30502:27017 --name container3 --net my-mongo-cluster mongo mongod --replSet my-mongo-set

//aqui configure o container1 como mestre, e os dois restantes como escravos na porta 27017, padrao do mongo
//configure container1 as master, the container2 and 3 as slaves on port 27017.
$config={"_id":"my-mongo-set","members":[{"_id":0,"host":"container1:27017"},{"_id":1,"host":"container2:27017"},{"_id":2,"host":"container3:27017"}]}

//inicialize a configuracao definida
//initialize config
$rs.initiate(config)

//mapear a porta 27017 pra que possa acessar a mesma dentro do container 
//map port 27017 so you can acces inside the container
$docker run -d -p 27017:27017 mongo

# //passo a passo de como executar:
# //How to exec your mongo cluster:

//Primeiramente você deve executar seus containers
//First of all you must run all the containers
$docker start container1 container2 container3

//Agora abra 3(três) terminais e em cada um executa 1(um) container no modo iterativo
//Now open 3(three) terminals and in each one execute 1(one) container on iterative mode 
$docker exec -it container1 mongo
$docker exec -it container2 mongo
$docker exec -it container3 mongo

//Deve aparecer algo como:
//terminal should looks like
my-mongo-set:PRIMARY>
my-mongo-set:SECONDARY>

//Em cada um dos terminais respectivamente você deve inicializar com
//on each terminal you should respectively initialize with
db = (new Mongo('container1:27017')).getDB('test')
db = (new Mongo('container2:27017')).getDB('test')
db = (new Mongo('container3:27017')).getDB('test')

//Agora você deve setar o container2 e o container3 como escravos(slave)
//Now you must set container2 and container3 as slaves
db.setSlaveOk()

//Pronto! divirta-se!
//Now it is ready! Have fun!

//Exemplos de operações com o mongo:
//Examples of operations on mongo:
db.Personagens.insert({"nome":'captain america',"raca":'human',"classe":'warrior',"vida":97})
db.Personagens.find()
db.Personagens.find().pretty()
db.Personagens.find().count()
db.Personagens.remove({})

//Se você deseja usar seu cluster de fora dos containers, utilize o pymongo. no arquivo geraCargaMongoDB.py, tem exemplos claros de como utilizar!
//If you want to use your cluster from outside it, you should use pymongo. The file geraCargaMongoDB.py has clear examples of how to use it! 
