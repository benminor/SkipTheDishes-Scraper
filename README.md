# SkipTheDishes-Scraper
A Python based data scraper to aggregate restaurant info from SkipTheDishes based on a particular city. The program utilizies BeautifulSoup4 and writes the data to a JSON file. The current data includes: Restaurant name, Delivery Time, and Rating value.

```json
{
    "7-Eleven": [
        {
            "Delivery Time": "13 to 23 mins",
            "Rating": "9.5"
        }
    ],
    "ABC Country Restaurant": [
        {
            "Delivery Time": "17 to 27 mins",
            "Rating": "9.8"
        }
    ],
    "Rickys Cafe": [
        {
            "Delivery Time": "27 to 37 mins",
            "Rating": "9.8"
        }
    ],
    "Ambit Cafe": [
        {
            "Delivery Time": "18 to 28 mins",
            "Rating": "9.7"
        }
    ]
}
```
