
from flask import Flask, render_template, request, redirect, url_for
import post_storage

app = Flask(__name__)

@app.route('/')
def index():
    blog_posts = post_storage.get_posts()
    return render_template('index.html', posts=blog_posts, title="Blog posts")



@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # We will fill this in the next step
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        post_storage.add_post(author, title, content)
        return redirect(url_for('index'))
    return render_template('add.html', title="Add your post")


@app.route('/delete/<int:post_id>')
def delete(post_id):
    # Find the blog post with the given id and remove it from the list
    post_storage.delete_post(post_id)
    # Redirect back to the home page
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    post = post_storage.fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
    # Update the post in the JSON file
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")
        post_storage.update_post(author, title, content, post_id)
    # Redirect back to index
        return redirect(url_for("index"))
    # Else, it's a GET request
    else:
        # So display the update.html page
        return render_template('update.html', post=post)



if __name__ == '__main__':
    app.run(port=5000, debug=True)
