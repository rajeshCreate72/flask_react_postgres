from flask import Blueprint, jsonify, request
from services.api_services import get_all_api_service, create_new_api_service
from models.api_model import Api 


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/request', methods=['GET'])
def get_api():
    try:
        api_all = get_all_api_service()

        if not api_all:
            return jsonify({'api_list': []})
        
        api_list = []
        

        for api_data in api_all:
            if isinstance(api_data, Api):
                api_list.append({
                    'id': api_data[0],
                    'request_id': api_data[1], 
                    'request_time': api_data[2],
                    'payload': api_data[3],
                    'content_type': api_data[4],
                    'ip_address': api_data[5],
                    'os': api_data[6],
                    'user_agent': api_data[7]
                })

        return jsonify({'api_list': api_list})
    except Exception as err:
        return jsonify({'error': str(err)}), 500

@api_blueprint.route('/request', methods=['POST'])
def post_api():
    api_data_from_client = request.json()
    create_new_api_service(
        api_data_from_client.get('request_id'),
        api_data_from_client.get('request_time'),
        api_data_from_client.get('payload'),
        api_data_from_client.get('content_type'),
        api_data_from_client.get('ip_address'),
        api_data_from_client.get('os'),
        api_data_from_client.get('user_agent')
    )
    return jsonify({'message': 'api data posted'}), 201

