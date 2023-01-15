import json

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def get_data():
    with open('posts.json', encoding='utf-8') as f:
        data = json.load(f)
    return data


def search_by_name(name):
    posts = []
    for post in get_data():
        if name in post["content"]:
            posts.append(post)
    return posts


def is_filename_allowed(filename):
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


def write_in_json(data):
    text = get_data()
    text.append(data)
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(text, f, indent=2, ensure_ascii=False)

