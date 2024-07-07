# This is a model, in a way stores the data in Database

class Api:
    def __init__(self,
                id,
                request_id, 
                request_time,
                payload,
                content_type,
                ip_address,
                os,
                user_agent
                 ):
        self.id = id
        self.request_id = request_id
        self.request_time = request_time
        self.payload = payload
        self.content_type = content_type
        self.ip_address = ip_address
        self.os = os
        self.user_agent = user_agent
        