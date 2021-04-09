from selenium.webdriver.common.by import By


class MainLocators (object):

    MAIN_CUSTOMER = (By.ID, 'ctl00_ContentPlaceHolder1_txtClient')
    MAIN_CUSTOMER_OUT = (By.ID, 'ctl00_ContentPlaceHolder1_btnNewIineraryWithoutClient')
    MAIN_CREATE_ITINERARY = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_btnCreateItinerary')


    #region Menu Administration
    MAIN_COUNTRY = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_1_cell')
    MAIN_CITY = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_1_cell')
    MAIN_AIRPORT = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_2_cell')
    MAIN_AIRLINE = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_3_cell')
    MAIN_TEAM = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_4_cell')
    MAIN_MAPPING = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_5_cell')
    MAIN_CACHE_HOTELS = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_6_cell')
    MAIN_PERMIT_USER_SERVICE = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_7_cell')
    MAIN_REPORT_TRANSACTION = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_8_cell')
    MAIN_DAILY_REPORT= (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_9_cell')
    MAIN_USER_SERVICE = (By.ID, 'ctl00_ContentPlaceHolder1_MainMenuControl_TreeView1_item_10_cell')
    #endregion Menu Administration


