import requests
from bs4 import BeautifulSoup

from database import save_product


url = "https://www.technolife.com/category/mobile/mobile-phone"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
cards = soup.select("section.relative.w-full.rounded-\\[10px\\]")


for card in cards:
    # Title
    title = card.find("h2").text.strip()
    # Image
    image = card.select_one("a[href^='/product-'] img").get("src")

    if image.startswith("/"):
        image = "https://www.technolife.com" + image
    # Product Link
    link = card.select_one('a[href^="/product-"]').get('href')
    link = "https://www.technolife.com" + link
    # Open Product Page
    product_response = requests.get(link)
    product_soup = BeautifulSoup(product_response.text,"html.parser")
    # Storage + RAM
    storage = None
    ram = None

    features = product_soup.select_one("div.rounded-md.border.border-solid.border-primary-tint-8.bg-white")

    if features != None:
        items = features.select("p.ml-1")
        for item in items:
            text = item.text.strip()
            if "Ú¯ÛŒÚ¯Ø§Ø¨Ø§ÛŒØª" in text:
                if storage == None:
                    storage = text
                else:
                    ram = text

    # Color
    color = None

    color_section = product_soup.select_one("div.mb-3\\.5.flex.items-center")

    if color_section != None:
        color = color_section.select("p")

        if len(color) > 1:
            color = color[1].text.strip()


    # Rating
    rating = None
    rating_section = product_soup.select_one("strong.cursor-pointer.p-4.text-5xl.text-primary-tint-1")

    if rating_section != None:
        rating = rating_section.text.strip()

    # Description
    description = None

    description_section = product_soup.select_one("div.review_content._d")

    if description_section != None:

        description_text = description_section.select("p")

        if len(description_text) > 0:
            description = description_text[0].text.strip()


    # Save Data in Database
    save_product(title,description,storage,ram,color,rating,image,link)

    # # Print Result
    # print("----------------------------")
    # print("Title:", title)
    # print("Image:", image)
    # print("Storage:", storage)
    # print("RAM:", ram)
    # print("Color:", color)
    # print("Rating:", rating)
    # print("Description:", description)
    # print("Link:", link)