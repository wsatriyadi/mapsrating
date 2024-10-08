from playwright.sync_api import sync_playwright
import time

class maps:
    def kasihrating(detail, proses, data):
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            page = browser.new_page()

            page.goto("https://accounts.google.com/")
            title = page.title()

            if(title == "Sign in - Google Accounts"):
                page.locator('//*[@id="identifierId"]').fill(data['user'])
                page.locator('//*[@id="identifierNext"]/div/button/div[3]').click()
                page.wait_for_selector('//*[@id="password"]/div[1]/div/div[1]/input', timeout=5000)
                page.locator('//*[@id="password"]/div[1]/div/div[1]/input').fill(data['password'])
                page.locator('//*[@id="passwordNext"]/div/button/span').click()
                try:
                    page.wait_for_selector('//*[@id="confirm"]', timeout=5000)
                    page.locator('//*[@id="confirm"]').click()
                except Exception as e:
                    #skip
                    print("sudah pernah login, skip")

            page.goto(detail['maps'])
            time.sleep(2)
            page.locator('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div/div/button[2]/div[2]').click()
            time.sleep(1)
            page.locator('//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[4]/div/button/span/span[2]').click()
            time.sleep(2)
            iframe = page.locator('//*[@name="goog-reviews-write-widget"]').content_frame
            iframe.locator('//*[@id="kCvOeb"]/div[1]/div[3]/div[1]/div[1]/div/div[2]/span[2]/span/div[1]/button/span[1]').click()
            iframe.locator('//*[@id="kCvOeb"]/div[1]/div[3]/div[1]/div[2]/div/div[5]').click()
            time.sleep(1)
            iframe.locator('//*[@id="kCvOeb"]/div[2]/div/div[2]/div/button/span').click()
            time.sleep(2)
            browser.close()
            print("selesai")
            #page.pause()
            #return title