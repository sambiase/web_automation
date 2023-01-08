def test_page_title(browser_init):
    browser_init.get('https://www.mockaroo.com/')
    assert 'Mockaroo - Random Data Generator and API Mocking Tool | JSON / CSV / SQL / Excel' in browser_init.title
