import requests

def hit_service(target):
    count = 1
    while count <= target:
        response = requests.api.get('https://ps-api-contentmanagement-blue.platform-dev.phreesia.services/v1/products/70e091a6-43c2-4a32-b693-7cf72d962ce6')
        # json = response.json()
        # print(json)
        print('hit: ', count)
        count = count + 1
        
continue_loop = True
while continue_loop:
    target_hits = int(input('how many hits to service ? \n'))
    hit_service(target_hits)
    user_input = input("Do you want to continue? Type 'n' or 'no' to stop: ").strip().lower()
    continue_loop = user_input not in ["n", "no"]
    print(continue_loop)
