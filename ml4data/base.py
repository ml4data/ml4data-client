import requests

class APIException(Exception):
    def __init__(self, msg, status_code):
        self.msg = msg
        self.status_code = status_code

    def __str__(self):
        return "[{status_code}] Error: {msg}".format(status_code=self.status_code,
                                                     msg=self.msg)

class AuthenticationError(APIException):
    def __init__(self, msg):
        super(AuthenticationError, self).__init__(msg, 401)


class ML4DataClient(object):
    """ Base class for all ML4Data clients
    """
    base_url = 'https://api.ml4data.com/api'
    def __init__(self, token):
        self.token = token
        self.session = requests.Session()
        self.session.headers = {"API-Key": self.token,
                                "User-Agent": 'ml4data-client'}

    def _make_request(self, method, endpoint, params=None, data=None, files=None):
        url = self.base_url + endpoint
        resp = self.session.request(url=url,
                                    method=method,
                                    params=params,
                                    data=data,
                                    files=files)
        if resp.status_code != 200:
            if resp.status_code == 401:
                raise AuthenticationError(resp.json()['error']['message'])
            else:
                raise APIException(resp.json()['error']['message'], status_code=resp.status_code)
        return resp.json()['result']

    def _get(self, endpoint, params=None, files=None):
        return self._make_request(method='GET',
                                  endpoint=endpoint,
                                  params=params,
                                  files=files)

    def _post(self, endpoint, params=None, data=None, files=None):
        return self._make_request(method='POST',
                                  endpoint=endpoint,
                                  params=params,
                                  data=data,
                                  files=files)

    def __del__(self):
        self.session.close()
