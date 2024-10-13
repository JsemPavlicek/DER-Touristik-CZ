# Test case :  Abstract - Using Python a Playwright for verification,
# haw many trips and which destinations are visible on the website
# https://www.dertouristik.cz/pruvodce/vylety

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.dertouristik.cz/')
    page.wait_for_load_state('networkidle')


    anchors_in_f_teaser_item_large = page.locator('div[class="f_teaser-item large"]')
    # print(anchors_in_f_teaser_item_large.count())

    for i in range(anchors_in_f_teaser_item_large.count()):
        one_anchor_text = anchors_in_f_teaser_item_large.nth(i).inner_text()
        # print(one_anchor_text)
        if "Průvodce a výlety" in one_anchor_text:
            anchors_in_f_teaser_item_large.nth(i).click()
            anchor_trips = page.locator('a[href="/pruvodce/vylety"]')
            anchor_trips.click()
            container_of_trips = page.locator('div.grd-container')
            trips = container_of_trips.locator('div[class="f_title"]')
            # print(trips.count())
    for i in range(trips.count()):
        trip_text = trips.nth(i).inner_text()
        print(f"{i + 1}. {trip_text}")
    print()
    print(f"{trips.count()} trip(s) is/are visible on the website https://www.dertouristik.cz/pruvodce/vylety")




    page.wait_for_timeout(3000)
    page.screenshot(path='pruvodce_a_vylety.png', full_page= True)

    browser.close()






