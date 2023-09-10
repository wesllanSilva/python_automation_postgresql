import psycopg2
import logging
import os
import json

# Leitura das configurações do arquivo config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Configurações dos bancos de dados
databases = config.get('databases', {})


# Configuração do log principal
logging.basicConfig(filename='LOGs/log_principal.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Função para conectar ao banco de dados
def connect_to_database(database_name):
    try:
        logging.info(f"Conectando ao banco de dados '{database_name}' ...")
        print(f"Conectando ao banco de dados '{database_name}' ...")
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database=database_name
        )
        logging.info(f"Conexao ao banco de dados '{database_name}' estabelecida com sucesso.")
        print(f"Conexao ao banco de dados '{database_name}' estabelecida com sucesso.")
        return connection
    
    except (Exception, psycopg2.Error) as error:
        logging.error(f"Erro ao conectar ao banco de dados '{database_name}': {error}")
        print(f"Erro ao conectar ao banco de dados '{database_name}': {error}")
        return None



# Função para executar a query de faturamento
def execute_update_query(connection, query, logger):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        row_count = cursor.rowcount
        connection.commit()
        logger.info(f"Query executada com sucesso, {row_count} linhas afetadas.")
    except (Exception, psycopg2.Error) as error:
        logger.error(f"Erro ao executar a query: {error}")

#configuração dos LOGs:
#configura um logger específico para um arquivo de log
def setup_logger(log_file):
    logger = logging.getLogger()  # Usar o logger principal
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

# Função principal
def main():
    for db_name, db_config in databases.items():
        log_dir = os.path.join('LOGs', db_name)
        os.makedirs(log_dir, exist_ok=True)

        update_queries = db_config.get('update_queries', [])
        if not update_queries:
            logging.warning(f"Nenhuma query de atualização definida para '{db_name}'. Pulando banco de dados.")
            continue

        connection = connect_to_database(db_name)
        if connection:
            for update_query in update_queries:
                with open(f'scripts/{update_query}', 'r') as f:
                    query = f.read()
                log_file = os.path.join(log_dir, f'{update_query[:-4]}.log')
                logger = setup_logger(log_file)
                try:
                    execute_update_query(connection, query, logger)
                except Exception as e:
                    logger.error(f"Erro ao executar a query: {str(e)}")
            connection.close()
   

if __name__ == "__main__":
    logging.info("Iniciando o script...")
    print("Iniciando o script...")
    main()
    logging.info("Script concluido.")
    print("Script concluído.")