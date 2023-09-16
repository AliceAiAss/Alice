from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID" : "ZwiipLo6S02ivZU-45kDBs8NpnfkyaK_YMeaB6fPrXEacXjz9hwAUWm6nl236UaCV6-kxA.",
    "__Secure-1PSIDTS" : "sidts-CjIBSAxbGTIQsGAzic_U3UqU1MBZljJjqkN9zq92FA4KyQdufEYDlvK5MHxlPArWGFPfSBAA",
    "__Secure-1PSIDCC" : "APoG2W8FETbte6kbh7gkUmy4gwtTxM2l-sjKZbNifmkQD_-sQivWNEjTPAqmrhfYdNzaqWiCnfI"
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    Query = input("Input your Query :")
    Reply = bard.get_answer(Query)['content']
    print(Reply)