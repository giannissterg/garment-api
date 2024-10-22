from pydantic import BaseModel, HttpUrl
from typing import Optional

class Image(BaseModel):
    url: HttpUrl
    path: str
    s3_url: HttpUrl
    s3_url_resized: HttpUrl

class Garment(BaseModel):
    gender: str
    product_id: str
    product_title: str
    product_description: str
    brand: str
    source: str
    product_categories: list[str]
    url: HttpUrl
    price: float
    discount: float
    currency_code: str
    stock: int
    stock_level: int
    additional_ids: list[str]
    image_urls: list[HttpUrl]
    position: list[Optional[str]]
    product_imgs_src: list[HttpUrl]
    images: list[Image]

# Example usage
product_data = {
    "gender": "men",
    "product_id": "AM0APBW00069FA650269_ΜΑΥΡΟ_AM0-9000",
    "product_title": "Μαγιό Σορτς ANTONY MORATO",
    "product_description": "Μαγιό Σορτς ANTONY MORATO σε μαύρο χρώμα με γκρι σχέδια, από γυαλιστερό ύφασμα. Διαθέτει 2 τσέπες στα πλάγια και μία τσέπη με καπάκι και κουμπί στο πίσω μέρος. Με λάστιχο και κορδόνι στη μέση. Διαθέτει εσωτερικά mesh σλιπ.",
    "brand": "ANTONY MORATO",
    "source": "shopntrade",
    "product_categories": ["ΑΝΔΡΙΚΟ > BEACHWEAR > SHORTS"],
    "url": "https://www.bloobox.gr/el-gr/andriko-beachwear-shorts/magio-sorts-antony-morato-633771",
    "price": 55.0,
    "discount": 0.4,
    "currency_code": "EUR",
    "stock": 1,
    "stock_level": 1,
    "additional_ids": ["AM0APBW00069FA650269_ΜΑΥΡΟ", "BW00069FA650269-9000"],
    "image_urls": [
        "https://www.bloobox.gr/Images/Products/Normal/630000/633771__3611227.jpg",
        "https://www.bloobox.gr/Images/Products/Normal/630000/633771.jpg",
        "https://www.bloobox.gr/Images/Products/Normal/630000/633771_2.jpg"
    ],
    "position": ["undefined", "undefined", "undefined"],
    "product_imgs_src": [
        "https://www.bloobox.gr/Images/Products/Normal/630000/633771__3611227.jpg",
        "https://www.bloobox.gr/Images/Products/Normal/630000/633771.jpg",
        "https://www.bloobox.gr/Images/Products/Normal/630000/633771_2.jpg"
    ],
    "images": [
        {
            "url": "https://www.bloobox.gr/Images/Products/Normal/630000/633771__3611227.jpg",
            "path": "images/a1620f40fedbd8ec79bf974630f0938ee6767e1d.jpg",
            "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/a1620f40fedbd8ec79bf974630f0938ee6767e1d.jpg",
            "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/a1620f40fedbd8ec79bf974630f0938ee6767e1d.jpg"
        },
        {
            "url": "https://www.bloobox.gr/Images/Products/Normal/630000/633771.jpg",
            "path": "images/8df998b6255f23e29cf8d6ce892b113641baa9e2.jpg",
            "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/8df998b6255f23e29cf8d6ce892b113641baa9e2.jpg",
            "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/8df998b6255f23e29cf8d6ce892b113641baa9e2.jpg"
        },
        {
            "url": "https://www.bloobox.gr/Images/Products/Normal/630000/633771_2.jpg",
            "path": "images/baa53d7e1ddbcf75e894668be5042c68e03f00b4.jpg",
            "s3_url": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/baa53d7e1ddbcf75e894668be5042c68e03f00b4.jpg",
            "s3_url_resized": "https://stylr-ai-engine-srv-data.s3-eu-west-1.amazonaws.com/srv/data/serving/resized/baa53d7e1ddbcf75e894668be5042c68e03f00b4.jpg"
        }
    ]
}

product = Garment(**product_data)
print(product)
