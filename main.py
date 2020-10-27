from tornado.options import define, options
from tornado import gen, httputil
from tornado.httpclient import *
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import logging
from tornado.web import Application
from tornado.log import access_log
from moesiftornado import MoesifMiddleware
from moesif_config import moesif_config

log = logging.getLogger(__name__)

define("port", default=8888, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps({ "msg": "Hello, world" }))

    def post(self):
        self.write(json.dumps({ "guid": "5f160998-bda7-4e01-acb1-5ad5dcdd2ffd", "isActive": False, "balance": "$2,388.61" }))

class CustomHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps({ "msg": "Hello, world from the custom handler" }))

    def post(self):
        self.write(json.dumps({ "symbol": "native", "me": -1763718629, "watch": 1915744029, "composed": "fourth" }))


class UsersHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.middleware = MoesifMiddleware(moesif_config)

    def post(self, id):
        user_profile = {
            'user_id': id,

            'campaign': {
                'utm_source': 'google',
                'utm_medium': 'cpc',
                'utm_campaign': 'adwords',
                'utm_term': 'api+tooling',
                'utm_content': 'landing'
            },
            'metadata': {
                'email': 'john@acmeinc.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'min': 10,
                'max': 100,
                'city': 'SF',
                'state': 'CA',
                'title': 'Software Engineer',
                'sales_info': {
                    'stage': 'Customer',
                    'lifetime_value': 24000,
                    'account_owner': 'mary@contoso.com'
                }
            }
        }

        self.middleware.update_user(user_profile)
        self.write(json.dumps({'user_id': id, 'update_users': 'success'}))
        self.set_status(201)

class CompaniesHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.middleware = MoesifMiddleware(moesif_config)

    def post(self, id):
        company_profile = {
            'company_id': id,
            'company_domain': 'acmeinc.com', # If domain is set, Moesif will enrich your profiles with publicly available info
            'campaign': {
                'utm_source': 'google',
                'utm_medium': 'cpc',
                'utm_campaign': 'adwords',
                'utm_term': 'api+tooling',
                'utm_content': 'landing'
            },
            'metadata': {
                'org_name': 'Acme, Inc',
                'plan_name': 'Free',
                'deal_stage': 'Lead',
                'mrr': 24000,
                'demographics': {
                    'alexa_ranking': 500000,
                    'employee_count': 47
                }
            }
        }

        self.middleware.update_company(company_profile)
        self.write(json.dumps({'company_id': id, 'update_companies': 'success'}))
        self.set_status(201)

def main():
    # Create a moesif middleware
    middleware = MoesifMiddleware(moesif_config)
    # Set the log_function to middleware.log_event to log the events to Moesif
    application = tornado.web.Application([(r"/", MainHandler), (r"/custom", CustomHandler), (r"/users/(.*)", UsersHandler), (r"/companies/(.*)", CompaniesHandler)], log_function=middleware.log_event)
    # Handle gzip request by passing decompress_request=True to the HTTPServer constructor 
    http_server = tornado.httpserver.HTTPServer(application, decompress_request=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
