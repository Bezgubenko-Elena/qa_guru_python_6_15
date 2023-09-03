"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have
from selene.support.shared import browser, config


@pytest.fixture(params=[(1920, 1080), (3840, 2160), (412, 915), (414, 896)],
                ids=['1920 * 1080', '3840 * 2160', '412 * 915', '414 * 896'])
def browser_size(browser_management, request):
    config.window_width, config.window_height = request.param


def test_github_desktop(browser_size):
    if config.window_width < 1012:
        pytest.skip("Test only for desktop")
    browser.open('https://github.com')
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser_size):
    if config.window_width >= 1012:
        pytest.skip("Test only for mobile")
    browser.open('https://github.com/')
    browser.element('.flex-1 button').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
