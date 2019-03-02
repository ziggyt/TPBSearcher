import random
import string

import bs4
import requests


PAGE_AMOUNT = 45
CONSTANTS = [3, 4]

results = []

USER = input("Enter user (CASE sensitive): ")
KEYWORD = input("Enter keyword: ")

for constant in CONSTANTS:
    for i in range(0, PAGE_AMOUNT):
        url = "https://thepiratebay.org/user/{}/{}/{}".format(USER, i, constant)
        print("Searched " + url)
        data = requests.get(url)
        soup = bs4.BeautifulSoup(data.text)
        links = soup.findAll(attrs={'class': 'detLink'})

        if len(links) is 0:
            print("REACHED LIMIT, CHECKING REVERSE UPLOAD HISTORY")
            break

        link: bs4.Tag
        for link in links:
            if KEYWORD in link.text.lower() and link.text not in results:
                results.append(" ")
                results.append(link.text)
                results.append("https://thepiratebay.org/{}".format(link.get("href")))



for res in results:
    print(res)

answer = input("Would you like to export the results? y/n")

if answer is "y":
    random_identifier = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    with open("{}_{}.txt".format(USER, random_identifier), "w") as output:
        for res in results:
            output.write(str(res))
            output.write("\n")

    input("Wrote results to file, press any key to continue")


