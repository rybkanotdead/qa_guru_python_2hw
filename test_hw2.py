import pytest
from selene import browser,have,be
from time import sleep



@pytest.fixture(autouse=True)
def browser_conf():
    browser.config.window_height = 1020
    browser.config.window_width = 1080
    browser.open('https://www.google.com/')
    yield
    browser.quit()


def test_suc_search():
    browser.element('[name="q"]').should(be.blank).type('kazakhstan').press_enter()
    sleep(10)
    browser.element('html').should(have.text('Страна, Центральная Азия'))

def test_unsuc_search():
    browser.element('[name="q"]').should(be.blank).type('asjdadffasfag').press_enter()
    sleep(10)
    browser.element('html').should(have.text('ничего не найдено'))
