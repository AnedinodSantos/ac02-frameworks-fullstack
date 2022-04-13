# ac02-frameworks-fullstack
Repositório para a entrega da atividade continua da matéria de fremeworks-fullstack

### Passo a passo efetuado
- docker pull mysql:5.7 -> comando para baixar a imagem
- docker run --name db -e MYSQL_ROOT_PASSWORD=dino1234 -p 3307:3307 -d mysql:5.7 -> comando para rodar o container com mysql
- docker network inspect bridge -> comando para verificar os IPs dos containers rodando
    - usaremos para acessar o mysql
- docker ps -> comando para ver os containers rodando
    - usaremos para pegar o id do container de mysql
- docker exec -it <id do container> /bin/bash -> fazemos isso para acessar o container e usar o bash
- mysql -uroot -p --host=172.17.0.* -> dentro do container acessamos o mysql conforme o IP exposto
    - dentro do mysql criamos o banco e a tabela
- exit -> para sair do bash
- exit -> para sair do container
- git clone -> para clonar um repositório com a aplicação flask para o docker
    - esse projeto tem que ter um Dockerfile devidamente configurado
    - devemos entrar no repositório clonado usado cd <nome do repositório>
- docker image build -t python-web . -> executamos esse comando de dentro do repositório
    - o docker vai executar os comando do Dockerfile criando uma imagem com esse repositório
- docker run --link db:db -p 5000:5000 -d python-web -> com esse comando rodamos a nossa imagem recém criada linkando ela com o container do banco mysql
- agora podemos acessar a porta 5000 que dá acesso a nossa aplicação

