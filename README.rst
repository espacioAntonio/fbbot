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


.. literalinclude:: fbbot/test/simpleEchoBot.py
   :language: python
   :emphasize-lines: 12,15-18
   :linenos:

5. Run `python3 simpleEchoBot.py` to collect files to test.

6. Start the development server and visit http://127.0.0.1:8000/webhook

7. Visit http://127.0.0.1:8000/webhook and see "Hello World, webhook enable"

8. Send a message to your facebook page and the Bot send the same text::


Uninstall
--------------------------------------------

1. If you want to uninstall this package run::

    pip uninstall fbbot

