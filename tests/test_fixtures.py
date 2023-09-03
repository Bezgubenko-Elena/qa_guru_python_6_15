"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have
from selene.support.shared import browser, config


@pytest.fixture()
def w_size_desktop(browser_management):
    config.window_width = 1920
    config.window_height = 1080


@pytest.fixture()
def w_size_mobile(browser_management):
    config.window_width = 414
    config.window_height = 896


def test_github_desktop(w_size_desktop):
    browser.open('https://github.com')
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(w_size_mobile):
    browser.open('https://github.com/')
    browser.element('.flex-1 button').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
