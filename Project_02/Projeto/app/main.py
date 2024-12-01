from flask import Flask
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados
DATABASE_URL = "postgresql://appuser:app_password@db:5432/app_db"

@app.route('/')
def home():
    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        
        # Alterar a consulta para a tabela 'registros'
        cursor.execute("SELECT * FROM registros;")
        rows = cursor.fetchall()  # Recupera os registros
        
        # Formatar os dados em HTML
        html = "<h1>Bem-vindo ao Projeto DevOps com Docker Compose!</h1>"
        html += "<h2>Dados do Banco:</h2><ul>"
        
        for row in rows:
            html += f"<li>ID: {row[0]}, Nome: {row[1]}</li>"
        
        html += "</ul>"
        
        return html
    except Exception as e:
        return f"Erro ao acessar o banco de dados: {e}"
    finally:
        # Fechar a conexão
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
