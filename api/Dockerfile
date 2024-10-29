#criar a img para rodar o container

#vai apontar para DockerHub
#FROM node:18-slim (antes, melhorando a performance, trocar a base image)
# 1 estagio
#FROM node:18-alpine3.19 AS build (para simular os estagio e tamanho da image tira essa )
FROM node:18 AS build


#diretorio base que quero rodar a aplicacao, diretorio de producao
WORKDIR /usr/src/app

#instalar a depend, se fosse npm ficaria package*.json, copiar arquivos sempre separa das pastas
#copiando da interface para o container
COPY package.json yarn.lock  .yarnrc.yml ./
#copiar pastas
COPY .yarn ./.yarn

RUN yarn install --immutable

#executar o gerenciador de pacotes (RUN yarn)
RUN yarn

#copy tudo da interface do container, e nao precisa do node_modules e dist, por isso criamos o dockerignore
COPY . .


#rodar o comando p execucao
RUN yarn run build
#ate aqui eh o build

#nao instala dev dependences, ajuda na reducao do tamanho da image (workspaces focus --production)
RUN yarn workspaces focus --production && yarn cache clean 
# e limpa o cache


#aqui para baixo eh executar a aplicacao
#outro estagio da aplicacao, build (outro FROM) - 2 estagio
FROM node:18-alpine3.19

#diretorio do 2 estagio poderia ser em outro diretorio, ex estagio 1 em um diretorio e o 2 em outro
WORKDIR /usr/src/app

#copiando de um estagio para outro estagio
#para rodar ./dist que foi gerado no RUN yarn run build
COPY --from=build /usr/src/app/package.json ./package.json
COPY --from=build /usr/src/app/dist ./dist
COPY --from=build /usr/src/app/node_modules ./node_modules


#porta para rodar
EXPOSE 3000

#subir a aplicacao
CMD [ "yarn", "run", "start:prod" ]
