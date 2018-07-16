import time
import logging
import requests

WEBSITE_LIST = [
    'http://envato.com',
    'http://amazon.co.uk',
    'http://amazon.com',
    'http://facebook.com',
    'http://google.com',
    'http://google.fr',
    'http://google.es',
    'http://google.co.uk',
    'http://internet.org',
    'http://gmail.com',
    'http://stackoverflow.com',
    'http://github.com',
    'http://heroku.com',
    'http://really-cool-available-domain.com',
    'http://djangoproject.com',
    'http://rubyonrails.org',
    'http://basecamp.com',
    'http://trello.com',
    'http://yiiframework.com',
    'http://shopify.com',
    'http://another-really-interesting-domain.co',
    'http://airbnb.com',
    'http://instagram.com',
    'http://snapchat.com',
    'http://youtube.com',
    'http://baidu.com',
    'http://yahoo.com',
    'http://live.com',
    'http://linkedin.com',
    'http://yandex.ru',
    'http://netflix.com',
    'http://wordpress.com',
    'http://bing.com',
]


class WebsiteDownException(Exception):
    pass


def ping_website(address, timeout=20):
    """
    Check if a website is down. A website is considered down
    if either the status_code >= 400 or if the timeout expires

    Throw a WebsiteDownException if any of the website down conditions are met
    """
    try:
        response = requests.head(address, timeout=timeout)
        if response.status_code >= 400:
            logging.warning("Website %s returned status_code=%s" % (address, response.status_code))
            raise WebsiteDownException()
    except requests.exceptions.RequestException:
        logging.warning("Timeout expired for website %s" % address)
        raise WebsiteDownException()


def notify_owner(address):
    """
    Send the owner of the address a notification that their website is down

    For now, we're just going to sleep for 0.5 seconds but this is where
    you would send an email, push notification or text-message
    """
    logging.info("Notifying the owner of %s website" % address)
    time.sleep(0.5)


def check_website(address):
    """
    Utility function: check if a website is down, if so, notify the user
    """
    try:
        ping_website(address)
    except WebsiteDownException:
        notify_owner(address)
