import time

from donation.donation import Donation

with Donation() as don:
    don.land_first_page()
    don.login_user("smridul191006@bscse.uiu.ac.bd", "Smridul!12@")
    time.sleep(2)
    don.view_campaign_card()
    don.donation_test(200)
while True:
    pass
