import requests

TEST_CAR = (
    "Mazda", "626", 562002.3, "Silver", "25JF8AS09FFK3952093",
    "fair", 1253.00, 1900.00, "It's silver.  And ugly.  But it runs.",
    "Placehold address", None, None
    )

def test_car_creation():
    out=requests.post("http://127.0.0.1:5000/register", json=TEST_CAR)
    if out.status_code == 201:
        print(out.json())
    else:
        print("Something wrong with creation")

if __name__ == "__main__":
    test_car_creation()