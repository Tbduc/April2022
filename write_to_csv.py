from email import header
import os

DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']

data = {"id": 15, "title": "takie title", "user_story": "test", "acceptance_criteria": "test criteria", "business_value": "test business value", "estimation": "test estimation", "status": "test status"}

def write_header(data:list):
    with open("data.csv", "w+") as file:
        file.write((",").join(data))
        
write_header(DATA_HEADER)

def write_data(data:dict):
    with open("data.csv", "a+") as file:
        file.write(f"\n{data['id']},{data['title']},{data['user_story']},{data['acceptance_criteria']},{data['business_value']},{data['estimation']}, {data['status']}")
        
write_data(data)

def read_status():
    user_stories = []
    with open("data.csv", "r+") as file:
        rows = file.readlines()
        headers = rows[0].strip().split(",")
        for row in rows[1::]:
            splitted_row = row.strip().split(",")
            story = {}
            for header, row in zip(headers, splitted_row):
                story[header] = row
            user_stories.append(story)
    print(user_stories)
read_status()
            