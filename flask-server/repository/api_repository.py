import psycopg2
from models.api_model import Api

def get_all_api():
    try:
        conn = psycopg2.connect(database="postgres", host="localhost", user="", password="", port="5432")
        curr = conn.cursor()
        curr.execute('''SELECT * FROM api_table;''')
        data = curr.fetchall()

        api_list = []

        for api_data in data:
            api = Api(
                id=api_data[0],
                request_id=api_data[1], 
                request_time=api_data[2],
                payload=api_data[3],
                content_type=api_data[4],
                ip_address=api_data[5],
                os=api_data[6],
                user_agent=api_data[7]
            )
            api_list.append(api)

        conn.close()
        curr.close()

        return api_list
    except psycopg2.Error as err:
        return (f"Error retriving data: {err}")
    
def create_new_api(
                request_id, 
                request_time,
                payload,
                content_type,
                ip_address,
                os,
                user_agent):
    try:
        conn = psycopg2.connect(database="postgres", host="localhost", user="", password="", port="5432")
        curr = conn.cursor()
        curr.execute('''INSERT INTO api_table 
                (
                request_id, 
                request_time,
                payload,
                content_type,
                ip_address,
                os,
                user_agent),
                VALUES(%s, %s, %s, %s, %s, %s, %s);
                ''', (request_id, request_time, payload, content_type, ip_address, os, user_agent))
        conn.close()
        curr.close()
        return "Api row created succesfully"
    except psycopg2.Error as err:
        return (f"Error creating api row: {err}")
