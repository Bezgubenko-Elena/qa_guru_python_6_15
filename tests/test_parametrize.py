"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have
from selene.support.shared import browser, config


@pytest.fixture(params=[(1920, 1080), (414, 896)])
def browser_size(browser_management, request):
    config.window_width, config.window_height = request.param


@pytest.mark.parametrize("browser_size", [(1920, 1080)], ids=['1920 * 1080'], indirect=True)
def test_github_desktop(browser_size):
    browser.open('https://github.com')
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_size", [(414, 896)], ids=['414 * 896'], indirect=True)
def test_github_mobile(browser_size):
    browser.open('https://github.com/')
    browser.element('.flex-1 button').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
