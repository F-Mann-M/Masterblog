import json


def load_file(file_path):
    """loads json and returns as list of dicts"""
    with open(file_path, "r") as handel:
        posts = json.load(handel)
        return posts

def get_post():
    """loads jason and returns list of dicts of the posts"""
    posts = load_file("data/post_data.json")
    # for post in posts:
    #     print(f"id: {post["id"]}, author: {post["author"]}, title: {post["title"]}")
    return posts

def get_new_post_id():
    posts = get_post()
    post_id = []
    for post in posts:
        post_id.append(post["id"])
    return max(post_id) + 1


def add_post(author, title, content):
    """load json, add new post along with author, title, content"""
    post_id = get_new_post_id()
    posts = get_post()
    new_post_dict = {"id": post_id, "author": author, "title": title, "content": content}
    posts.append(new_post_dict)
    write_file(posts)



def write_file(file):
    with open("data/post_data.json", "w") as handel:
        json.dump(file, handel)