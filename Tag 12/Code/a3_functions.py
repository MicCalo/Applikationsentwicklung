from flask.wrappers import Request
from logging.config import dictConfig

from datetime import datetime
import platform

datetime_format = "%a, %d. %b %Y %H:%M:%S"

def get_infos_from_request(request: Request):
    """Gathers some information from the request and returns them as a dictionary."""
    return {
        'method': request.method,
        'user_agent': request.user_agent.string,
        'languages': request.accept_languages,
        'encodings': request.accept_encodings,
        'url': request.base_url,
        'client IP': request.remote_addr
    }


def get_server_infos():
    """Gathers some information about the platform this server is running on"""
    return {
        'platform': platform.platform(), 
        'startup_time':get_current_time_str(),
        'served_requests': '0'
    }
    

def increment_served_requests_counter(server_infos: dict[str, str]):
    server_infos['served_requests'] = str(int(server_infos['served_requests']) + 1)


def setup_logging():
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s : %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })


def get_current_time_str():
    return datetime.now().strftime(datetime_format)