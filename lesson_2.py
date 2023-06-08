from selene import be, have, browser
import pytest

@pytest.fixture()
def size_window():
    browser.config.window_width = 1440
    browser.config.window_height = 2160

@pytest.fixture()
def open_url():
    browser.open('https://google.com')


def test_google_search(size_window, open_url):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_invalid_google_search(size_window, open_url):
    request = 'dn75bw87vbti6nvb'
    browser.element('[name="q"]').should(be.blank).type(request).press_enter()
    browser.element('[id="res"]').should(have.text(f'По запросу {request} ничего не найдено'))
