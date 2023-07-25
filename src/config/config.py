from sqlalchemy import create_engine
import json
import os
import sys

class SQLConnection:
    @staticmethod
    def read_credentials():
        cred_file = os.path.join(f'{os.getcwd()}/etl_pipelines/config/local.json')
        with open(cred_file) as f:
            data = json.load(f)
        return data

    @staticmethod
    def engine_instance():
        data = SQLConnection.read_credentials()
        return create_engine(f"postgresql://{data['user']}:{data['password']}@{data['host']}:{data['port']}/processed_{data['dbname']}"+f"_{sys.argv[1]}")
