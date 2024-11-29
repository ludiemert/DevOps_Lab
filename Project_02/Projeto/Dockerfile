# Escolha uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Instale as dependências do sistema necessárias para compilar o dlib
RUN apt-get update -o Acquire::ForceIPv4=true && apt-get install -y \
    build-essential \
    cmake \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copie os arquivos de requisitos (requirements.txt) para o diretório de trabalho no container
COPY requirements.txt .

# Atualize o pip para a versão mais recente
RUN pip install --upgrade pip

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo da pasta local (no host) para dentro do container
COPY . .

# Defina o comando padrão para rodar o aplicativo
CMD ["python", "main.py"]
