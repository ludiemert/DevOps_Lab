#criar a img para rodar o container

#vai apontar para DockerHub
FROM node:18-slim

#diretorio base que quero rodar a aplicacao
WORKDIR /usr/src/app


#instalar a depend
COPY package.json ./

#executar o gerenciador de pacotes
RUN yarn

#copy tudo da interface do container
COPY . .


#rodar o comando p execucao
RUN yarn run build

#porta para rodar
EXPOSE 3000

#subir a aplicacao
CMD [ "yarn", "run", "start" ]
