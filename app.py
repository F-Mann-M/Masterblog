
from flask import Flask, render_template, request, redirect, url_for
from matplotlib.pyplot import title

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



if __name__ == '__main__':
    app.run(port=5000, debug=True)
