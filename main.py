import web_data
import get_store_numbers as item_price
import asyncio

# click on cookie as fast as possible
async def click_on_cookie():
    while True:
        cookie = web_data.driver.find_element_by_id("cookie")
        cookie.click()
        task = asyncio.create_task(check())
        await task

# check panel every five second to see which one is affordable
async def check():
    if item_price.current_money() > item_price.cursor_price() and item_price.cursor_price() < item_price.gran_price():
        click_cursor = web_data.driver.find_element_by_id(item_price.cursor)
        click_cursor.click()

    elif item_price.current_money() > item_price.gran_price() and item_price.gran_price() < item_price.fact_price():
        click_cursor = web_data.driver.find_element_by_id(item_price.gran)
        click_cursor.click()

    elif item_price.current_money() > item_price.fact_price() and item_price.fact_price() < item_price.mine_price():
        click_cursor = web_data.driver.find_element_by_id(item_price.fact)
        click_cursor.click()

    elif item_price.current_money() > item_price.mine_price() and item_price.mine_price() < item_price.ship_price():
        click_cursor = web_data.driver.find_element_by_id(item_price.mine)
        click_cursor.click()

    elif item_price.current_money() > item_price.ship_price() and item_price.ship_price() < item_price.alchemy_price():
        click_cursor = web_data.driver.find_element_by_id(item_price.ship)
        click_cursor.click()

    elif item_price.current_money() > item_price.alchemy_price() and item_price.alchemy_price() < item_price.portal_price():
        click_cursor = web_data.driver.find_element_by_id(item_price.alchemy)
        click_cursor.click()

    elif item_price.current_money() > item_price.portal_price() and item_price.portal_price() < item_price.time_machine():
        click_cursor = web_data.driver.find_element_by_id(item_price.portal)
        click_cursor.click()

    elif item_price.current_money() > item_price.time_machine():
        click_cursor = web_data.driver.find_element_by_id(item_price.time)
        click_cursor.click()
    else:
        print("Not Enough")

asyncio.run(click_on_cookie())
