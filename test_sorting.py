from playwright.sync_api import sync_playwright

def test_price_sorting():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open SauceDemo
        page.goto("https://www.saucedemo.com/")
        page.fill('[data-test="username"]', 'standard_user')
        page.fill('[data-test="password"]', 'secret_sauce')
        page.click('[data-test="login-button"]')

        # Wait for inventory page
        page.wait_for_selector('.inventory_list')
        page.wait_for_timeout(2000)

        # Select "Price: Low to High"
        dropdown = page.locator('//select[@class="product_sort_container"]')
        dropdown.select_option("lohi")
        page.wait_for_timeout(3000)

        # Extract and verify prices
        price_elements = page.locator('.inventory_item_price').all_text_contents()
        prices = [float(price.replace("$", "")) for price in price_elements]
        page.wait_for_timeout(5000)

        # Assertion for sorting
        assert prices == sorted(prices), f"Sorting failed! Prices: {prices}"

        print("Sorting Verified Successfully!")

        browser.close()

# Run the test
test_price_sorting()
