def test_page_title(browser_init):
    browser_init.get('https://www.mockaroo.com/')
    assert 'Mockaroo - Random Data Generator and API Mocking Tool | JSON / CSV / SQL / Excel' in browser_init.title

def test_browser_type(browser_init):
    browser_init.get('https://www.mockaroo.com/')
    assert 'chrome' in browser_init.name.lower()

