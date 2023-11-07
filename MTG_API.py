import MTG_CV
import requests
import urllib.request


def searchForCard(inputImage):
    final_ID = 0
    value = 0
    query = MTG_CV.findText('name.jpg', 0)
    # %3A == "="
    # for requesting from API
    # dataraw = requests.get(f"https://api.scryfall.com/cards/search?q=o:{query}")
    dataraw = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={query}")
    data = dataraw.json()
    print(data)

    try:
        cardArt = data['image_uris']['art_crop']
    except:
        try:
            for x in data['card_faces']:
                cardArt = x['image_uris']['art_crop']
        except:
            query = MTG_CV.findText('fullname.jpg', 0)
            dataraw = requests.get(f"https://api.scryfall.com/cards/named?fuzzy={query}")
            data = dataraw.json()
            print(data)
            try:
                cardArt = data['image_uris']['art_crop']
            except:
                try:
                    for x in data['card_faces']:
                        cardArt = x['image_uris']['art_crop']
                except:
                    try:
                        query = MTG_CV.findText('bottom.jpg', 1)
                        dataraw = requests.get(f"https://api.scryfall.com/cards/search?q=o:{query}")
                        data = dataraw.json()
                        print(data)
                        for i in data['data']:
                            tempval = 0

                            # the below blurb extracts the card ID and image
                            ID = i['id']
                            try:
                                imageURI = i['image_uris']
                            except:
                                for x in i['card_faces']:
                                    imageURI = x['image_uris']
                            cardArt = imageURI['art_crop']

                            # writes the card art to art.jpg
                            urllib.request.urlretrieve(cardArt, "art.jpg")

                            # calls the CV comparision function
                            # and if the value is the highest so far
                            # then it becomes the current best
                            tempval = MTG_CV.compare(inputImage, "art.jpg")
                            if tempval > value:
                                value = tempval
                                final_ID = ID
                    except:
                        print('Your card was not found in the Scryfall database.')

    # writes the card art to art.jpg
    urllib.request.urlretrieve(cardArt, "art.jpg")

    # calls the CV comparision function
    # and if the value is the highest so far
    # then it becomes the current best
    tempval = MTG_CV.compare(inputImage, "art.jpg")


    # this outputs the final card, might change to separate function
    try:
        name_data = requests.get(f"https://api.scryfall.com/cards/{final_ID}").json()
        name = name_data['name']
    except:
        name = data['name']
    urllib.request.urlretrieve(cardArt, "art.jpg")
    return name
