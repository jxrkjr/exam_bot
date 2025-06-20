from os import getenv
from dotenv import load_dotenv

load_dotenv()

PG_USER = getenv('PG_USER')
PG_DB = getenv('PG_DB')
PG_PASS = getenv('PG_PASS')
PG_HOST = getenv('PG_HOST')
PG_PORT = getenv('PG_PORT')


if __name__ == '__main__':
    print(PG_USER)
    print(PG_DB)
    print(PG_PASS)
    print(PG_HOST)
    print(PG_PORT)
