import requests
import urllib


class ApiClient():

    def __init__(self, username, password, base_url, host=None):
        """
        Initializes the options
        """
        self.host = host
        self.username = username
        self.password = password
        self.base_url = base_url
        self.session = self.get_server_session(self.username, self.password)
        import requests.packages as test
        test.urllib3.disable_warnings()

    def get_server_session(self, username, password):
        """
        Creating REST client session for server connection,
        after globally setting
        Authorization, Content-Type and charset for session.
        """
        session = requests.Session()
        session.auth = (username, password)
        session.verify = False
        session.headers.update(
            {'Content-Type': 'application/json; charset=utf-8'})
        return session

    def _url(self, base_url, path, res_id, params):
        """
        Helper method to generate a URL from a base,
        relative path, and dictionary
        of query parameters.
        """
        if params:
            return "%s/%s?%s" % (base_url, path, urllib.urlencode(params))
        elif res_id:
            return "%s/%s/%s" % (base_url, path, res_id)
        else:
            return "%s/%s" % (base_url, path)

    # def jira_issue_url(self, path, *res_id, **params):
    #     """
    #     Method to create jira issue url
    #     """
    #     url = self._url(self.base_url, path, res_id, params)
    #     print url
    #     return url

    def get_task(self, path, res_id, **params):
        """
        Generic get req
        """
        url = self._url(self.base_url, path, res_id, params)
        print url
        return self.session.get(url)


if __name__ == '__main__':
    rst = ApiClient(username="anupam.debnath@alefmobitech.com",
                    password="",
                    base_url="https://alefmobitech.atlassian.net/rest/api/2")
    params = {'jql': ['assignee=fred'], 'startAt': ['2'], 'maxResults': ['2']}
    res_id = "anup"
    print(rst.get_task(path="createmeta", res_id="anup"))
