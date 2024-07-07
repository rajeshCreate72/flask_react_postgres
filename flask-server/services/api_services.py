from repository.api_repository import get_all_api, create_new_api

def get_all_api_service():
    return get_all_api()

def create_new_api_service(
                request_id, 
                request_time,
                payload,
                content_type,
                ip_address,
                os,
                user_agent):
    return create_new_api(
                request_id, 
                request_time,
                payload,
                content_type,
                ip_address,
                os,
                user_agent)
