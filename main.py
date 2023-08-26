import time

from donation.donation import Donation

with Donation() as don:
    don.land_first_page()
    don.login_user("smridul191006@bscse.uiu.ac.bd", "Smridul!12@")
    don.view_campaign_card()
    current_donation = don.get_previous_donation_value()
    don.set_donation_amount(300)
    don.select_anonymous_checkbox(0)
    don.click_donate_button()
    don.set_card_info("4242424242424242", "1232", "133", "12121")
    don.donation_test()
    don.check_donation_update(current_donation, 300)

while True:
    pass
