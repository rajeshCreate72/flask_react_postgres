# This is for connecting to database and creating tables

import psycopg2

try:
    connect = psycopg2.connect(database="postgres", host="localhost", user="", password="", port="5432")

    current = connect.cursor()

    api_query = '''
                    CREATE SEQUENCE custom_id_seq START 1;
                    CREATE TABLE IF NOT EXISTS api_table(
                        id TEXT PRIMARY KEY DEFALULT 'R' || LPAD(nextval('Rcustom_id_seq')::VARCHAR, 3, '0'),
                        request_id varchar(50) not null,
                        request_type varchar(10) not null,
                        request_time varchar(50) not null,
                        payload TEXT,
                        ip_address varchar(20) not null,
                        os varchar(20) not null,
                        user_agent varchar(20) not null
                    );
                    '''

    current.execute(api_query)

    connect.commit()
except psycopg2.Error as err:
    print(f"Error creating table: {err}")

finally:
    current.close()
    connect.close()