===============================
Facebook Messenger Bot : fbbot
===============================

fbbot is a sim1ple bot class to showcasing the Messenger Platform, make your facebook bot with django-fbbot

Install
----------------------------------------

1. Install **fbbot** package with python-pip::

    pip install fbbot

2. Add your valid tokens in your script file ::

    FB_PAGE_TOKEN = "FACEBOOK_PAGE_TOKEN"
    FB_VERIFY_TOKEN = "VERIFY_TOKEN_DEFINED_BY_DEVELOPER"
    REAL_URL = "URL_PROVIDED_FOR_NGROK" #example: 12346578.ngrok.io or www.yourdomain.com
    BASE_URL = "https://"+REAL_URL

3. Add your facebook bot::

    from fbbot.bot import Bot
    myBot = Bot(FB_PAGE_TOKEN, BASE_URL)

4. Simple EchoBot example "simpleEchoBot.py"::

    import json
    from pprint import pprint
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from fbbot.bot import Bot
    
    FB_VERIFY_TOKEN = "VERIFY_TOKEN_DEFINED_BY_DEVELOPER"
    FB_PAGE_TOKEN = "FACEBOOK_PAGE_TOKEN"
    BASE_URL = "URL_PROVIDED_FOR_NGROK" #example: https://12346578.ngrok.io or https://www.yourdomain.com
    
    
    # HTTPRequestHandler class
    class TestRequestHandler(BaseHTTPRequestHandler):
        myBot = Bot(FB_PAGE_TOKEN, BASE_URL)
    
        def do_GET(self):
            print(self.path)
            message = "default message"
            if self.path.startswith('/webhook'):
                query = urlparse(self.path).query
                query = dict(qc.split("=") for qc in query.split("&"))
                if 'hub.verify_token' in query and query['hub.verify_token'] == FB_VERIFY_TOKEN:
                    message = query['hub.challenge']
                else:
                    message = "Hello World, webhook enable"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(message, "utf8"))
            return
    
        def do_POST(self):
            if self.path.startswith('/webhook'):
                content_len = int(self.headers.get('Content-Length'))
                post_body = self.rfile.read(content_len)
                pprint(":: post_body ::")
                pprint(post_body)
                incoming_message = json.loads(str(post_body, 'utf-8'))
                if 'object' in incoming_message and incoming_message['object'] == 'page':
                    for entry in incoming_message['entry']:
                        for message in entry['messaging']:
                            pprint(":: message ::")
                            pprint(message)
                            for message_type in self.myBot.message_type_functions:
                                if message_type in message:
                                    self.myBot.message_type_functions[message_type](message)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("ok", "utf8"))
            return
    
    
    def run():
        print('starting server...')
        server_address = ('127.0.0.1', 8080)
        httpd = HTTPServer(server_address, TestRequestHandler)
        print('running server...')
        httpd.serve_forever()
    
    run()


5. Run `python3 simpleEchoBot.py` to collect files to test.

6. Start the development server and visit http://127.0.0.1:8000/webhook

7. Visit http://127.0.0.1:8000/webhook and see "Hello World, webhook enable"

8. Send a message to your facebook page and the fbbot send the same text::

            Hello! :User
    Bot: Hello!
             Echo! :User
    Bot: Echo!

Uninstall
--------------------------------------------

1. If you want to uninstall this package run::

    pip uninstall fbbot

