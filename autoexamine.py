import pyautogui as pyg
import time

# Trader position 0,0
traderPos = [705, 415]

# Item position 0,0
itemPos = [35, 290]


# For each trader select the trader and examine all items
def navigate_traders(trader):
    rows = [0, 1]
    columns = [0, 1, 2, 3]
    for row in rows:
        for column in columns:
            print(row, column)
            time.sleep(3)
            pyg.moveTo(traderPos[0] + (column * 175), traderPos[1] + (row * 215))
            pyg.click()
            time.sleep(1)
            trader = trader + 1
            examine_items(trader)


# Examines all visible items in traders inventory
def examine_items(trader):
    print(f"Trader is: {trader}")
    columns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    # Therapist has the smallest inventory so reduce rows when examining her stuff
    if trader == 1:
        rows = [0, 1, 2, 3]

    for row in rows:
        for column in columns:
            pyg.moveTo(itemPos[0] + (column * 63), itemPos[1] + (row * 63))
            pyg.middleClick()
            time.sleep(1.2)

    pyg.keyDown("ESC")
    pyg.keyUp("ESC")


navigate_traders(-1)
