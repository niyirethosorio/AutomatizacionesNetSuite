from selenium.webdriver.common.by import By


class NetFullFillmentLocator(object):

    MAIN_MENU_AIR = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_lblAirTitle')
    MAIN_MENU_HOTEL = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_lblHotelTitle')
    MAIN_MENU_HOTEL_AIR = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_lblAirHotelTitle')
    MAIN_MENU_HOTEL_BUS = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_lblHotelBusTitle')
    MAIN_MENU_BUS = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_lblBusTitle')
    MAIN_MENU_EXTRA = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_lblExtraTitle')
    MAIN_CAR = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_lblCarTitle')
    MAIN_CAR_AIR = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_lblAirCarTitle')

    #region Hotels
    MAIN_DESTINATION = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_txtCityDestination')
    MAIN_CHECK_IN = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_txtCheckIn')
    MAIN_CHECKOUT = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_txtCheckOut')
    MAIN_NIGHT = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_txtNights')
    MAIN_ROOM_COUNT = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ddlRoomsCount_Hotel')
    MAIN_ADULT_COUNT = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ddlAdults1_Hotel')
    MAIN_CHILD_COUNT = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ddlChilds_Hotel')
    MAIN_SEARCH_HOTEL = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_btnQuoteHotel')
    #endregion Hotels
    #region Air
    MAIN_RBN_RT = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_rbnRT')
    MAIN_RBN_OW = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_rbnOW')
    MAIN_RBN_MD = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_rbnMD')
    MAIN_TXT_ORIGIN = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_txtOrigin')
    MAIN_TXT_DESTINATION = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_txtDestination')
    MAIN_TXT_START_DATE = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_txtStartDate ')
    MAIN_TXT_END_DATE = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_txtEndDate ')
    MAIN_COUNT_ADULT = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ddlAdults ')
    MAIN_COUNT_CHILD = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ddlChilds ')
    MAIN_COUNT_INFANTS = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_ddlInfants ')
    MAIN_RBN_AIR_QUOTE = (By.ID, 'ctl00_ctl00_NetSiteContentPlaceHolder_NetFulfillmentContentPlaceHolder_btnAirQuote ')
    #endregion Air








