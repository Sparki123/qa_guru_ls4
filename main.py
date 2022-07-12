def func_description(func, ):
    print(func.__name__)
    print(func.__code__.co_varnames)
    print('***')


def open_browser(browser_name):
    func_description(open_browser)
    pass


def go_to_companyname_homepage(page_url):
    func_description(go_to_companyname_homepage)
    pass


def find_registration_button_on_login_page(page_url, button_text):
    func_description(find_registration_button_on_login_page)
    pass


open_browser((1, 2))
go_to_companyname_homepage(["Yasuo", "Kaisa", "Jinx"])
find_registration_button_on_login_page(open_browser, go_to_companyname_homepage)