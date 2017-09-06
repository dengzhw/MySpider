import random
from scrapy.utils.project import get_project_settings
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent
        self.user_agent_list = get_project_settings().get("USER_AGENT_LIST")

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        print ("user-agent"+ua)
        if ua:
            request.headers.setdefault('User-Agent', ua)
