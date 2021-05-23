import web_data

#store IDs and list
cursor = "buyCursor"
gran = "buyGrandma"
fact = "buyFactory"
mine = "buyMine"
ship = "buyShipment"
alchemy = "buyAlchemy lab"
portal = "buyPortal"
time = "buyTime machine"
store = [cursor, gran, fact, mine, ship]

# money that I have
def current_money():
    money = web_data.driver.find_element_by_id("money")
    money = money.text
    money = int(money)

    return money

#returns the price of five store items
def cursor_price():
        upgrade = web_data.driver.find_element_by_id(cursor)
        upgrade = upgrade.text
        upgrade = upgrade.split(" ")[2]
        upgrade = upgrade.split("\n")[0]
        upgrade = upgrade.replace(",", "")
        upgrade = int(upgrade)

        return upgrade

#returns the granny price item
def gran_price():
    upgrade = web_data.driver.find_element_by_id(gran)
    upgrade = upgrade.text
    upgrade = upgrade.split(" ")[2]
    upgrade = upgrade.split("\n")[0]
    upgrade = upgrade.replace(",", "")
    upgrade = int(upgrade)

    return upgrade

#returns the factory price item
def fact_price():
    upgrade = web_data.driver.find_element_by_id(fact)
    upgrade = upgrade.text
    upgrade = upgrade.split(" ")[2]
    upgrade = upgrade.split("\n")[0]
    upgrade = upgrade.replace(",", "")
    upgrade = int(upgrade)

    return upgrade

#returns the mine price item
def mine_price():
    upgrade = web_data.driver.find_element_by_id(cursor)
    upgrade = upgrade.text
    upgrade = upgrade.split(" ")[2]
    upgrade = upgrade.split("\n")[0]
    upgrade = upgrade.replace(",", "")
    upgrade = int(upgrade)

    return upgrade

#returns the ship price item
def ship_price():
    upgrade = web_data.driver.find_element_by_id(gran)
    upgrade = upgrade.text
    upgrade = upgrade.split(" ")[2]
    upgrade = upgrade.split("\n")[0]
    upgrade = upgrade.replace(",", "")
    upgrade = int(upgrade)

    return upgrade

#returns the price of the alchemy item
def alchemy_price():
    upgrade2 = web_data.driver.find_element_by_id(alchemy)
    upgrade2 = upgrade2.text
    upgrade2 = upgrade2.split(" ")[3]
    upgrade2 = upgrade2.split("\n")[0]
    upgrade2 = upgrade2.replace(",", "")
    upgrade2 = int(upgrade2)

    return upgrade2

#returns the price of the portal item
def portal_price():
    upgrade2 = web_data.driver.find_element_by_id(portal)
    upgrade2 = upgrade2.text
    upgrade2 = upgrade2.split(" ")[2]
    upgrade2 = upgrade2.split("\n")[0]
    upgrade2 = upgrade2.replace(",", "")
    upgrade2 = int(upgrade2)

    return upgrade2

#returns the price of the time machine item
def time_machine():
    upgrade2 = web_data.driver.find_element_by_id(time)
    upgrade2 = upgrade2.text
    upgrade2 = upgrade2.split(" ")[3]
    upgrade2 = upgrade2.split("\n")[0]
    upgrade2 = upgrade2.replace(",", "")
    upgrade2 = int(upgrade2)

    return upgrade2
