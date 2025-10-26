import os
class Config:
    # Outras configurações...
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'rrssouza.mysql.pythonanywhere-services.com')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'rrssouza')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '02090702Sou*')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'rrssouza$dbgestaoteen')

    # Definir diretamente a URI de conexão como uma string
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False