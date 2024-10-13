import os
import configparser


class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, 'config.properties')

        config = configparser.ConfigParser()
        config.read(config_path)

        db_config = config['DatabaseConfig']
        connection_string = {
            'host': db_config['db_url'],
            'port': db_config.getint('db_port'),
            'database': db_config['db_name'],
        }

        return connection_string