import cloudpassage
from ..config import CONFIG


class Api(object):
    def __new__(cls):
        session = cloudpassage.HaloSession(
            CONFIG['key_id'],
            CONFIG['secret_key'],
            api_port=CONFIG["api_port"],
            api_host=CONFIG["api_hostname"]
        )
        return cloudpassage.HttpHelper(session)
