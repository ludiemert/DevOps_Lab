# Usar a imagem oficial do Python
FROM python:3.10-slim

# Instalar dependências de compilação
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos da pasta local (host) para o container
COPY app/ /app/

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta que a aplicação irá rodar
EXPOSE 5000

# Definir o comando para rodar o Flask
CMD ["python", "main.py"]
