from fastapi import FastAPI
from enum import Enum

food_items = {
    'indian' : ['samosa', 'dosa'],
    'american': ['hot dog', 'apple pie'],
    'italian' : ['pizza']
}
class AvailableCuisines(str, Enum):
    indian = 'indian'
    american = 'american'
    italian = 'italian'

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

app = FastAPI()

valid_cuisines = food_items.keys()
@app.get("/get_items/{cuisine}")
async def read_root(cuisine):
    # doing validation ourselves
    # if cuisine not in valid_cuisines:
    #     return f'avaialble cuisines {valid_cuisines}'
    # else:
    #     return food_items.get(cuisine)
    return food_items.get(cuisine)

# fast api gives validation for free

@app.get("/get_food_by_cuisine/{cuisine}")
async def get_items_enum(cuisine: AvailableCuisines):
    return food_items.get(cuisine)



@app.get("/get_coupons/{code}")
async def get_coupons(code: int):
    return f'discount is {coupon_code.get(code)}'