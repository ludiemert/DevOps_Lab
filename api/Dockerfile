#criar a img para rodar o container

#vai apontar para DockerHub
FROM node:18-slim

#diretorio base que quero rodar a aplicacao
WORKDIR /usr/src/app


#instalar a depend, se fosse npm ficaria package*.json, copiar arquivos sempre separa das pastas
COPY package.json yarn.lock  .yarnrc.yml ./
#copiar pastas
COPY .yarn ./.yarn

RUN yarn install --immutable

#executar o gerenciador de pacotes
RUN yarn

#copy tudo da interface do container, e nao precisa do node_modules e dist, por isso criamos o dockerignore
COPY . .


#rodar o comando p execucao
RUN yarn run build

#porta para rodar
EXPOSE 3000

#subir a aplicacao
CMD [ "yarn", "run", "start" ]
