class ExpectedResponseDataset:
    PREORDER_BOOK_RESPONSE = {
        "data": {
            "addBonuses": 25,
            "bonusPayment": 0,
            "cost": 1019,
            "costWithSale": 832,
            "discount": 187,
            "maxBonusPayment": 0,
            "product": {
                "adData": {
                    "item_list_name": "",
                    "product_shelf": ""
                },
                "authors": [
                    {
                        "firstName": "Ромен",
                        "id": 12839,
                        "isForeignAgent": False,
                        "lastName": "Гари",
                        "middleName": "",
                        "url": "gari-romen-12839"
                    }
                ],
                "category": {
                    "id": 110002,
                    "slug": "sovremennaya-proza",
                    "title": "Современная проза",
                    "url": "sovremennaya-proza-110002"
                },
                "categoryChain": [
                    "Книги",
                    "Художественная литература",
                    "Современная проза"
                ],
                "coauthors": [],
                "cost": 832,
                "disabledBonuses": False,
                "fullCost": 1019,
                "fullPrice": 1019,
                "goodsId": 3044076,
                "id": 0,
                "inSubscription": False,
                "isBook": True,
                "isBookmarks": False,
                "isMagic": False,
                "nForM": None,
                "picture": "pim/products/images/33/17/018fd216-68f4-7a35-a40c-5bd23cba3317.jpg",
                "preOrder": False,
                "price": 832,
                "publisher": "АСТ",
                "quantity": 1,
                "sale": False,
                "status": "",
                "stock": 1,
                "title": "Воздушные змеи",
                "url": "product/vozdushnye-zmei",
                "weight": 390
            },
            "weight": 390
        }
    }

    DELETE_NON_EXIST_BOOK_RESPONSE = {
        "message": "товар в корзине не найден",
        "requestId": "95a4c071a1805ae5be1911ec4af6168b"
    }

    BAD_REQUEST_RESPONSE = {
        "message": "EOF",
        "requestId": "080210d53546b0e83bdff3c0281a3fb1"
    }
