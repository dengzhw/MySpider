import random
from scrapy.utils.project import get_project_settings
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
import base64
from settings import PROXIES

class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent
        self.user_agent_list = get_project_settings().get("USER_AGENT_LIST")

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        print ("user-agent"+ua)
        if ua:
            request.headers.setdefault('User-Agent', ua)

class ProxyMiddleware(object):

    def process_request(self, request, spider):

        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:

            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

            print "**************ProxyMiddleware have pass************" + proxy['ip_port']

        else:
            print "**************ProxyMiddleware no pass************" + proxy['ip_port']
            request.meta['proxy'] = "http://%s" % proxy['ip_port']