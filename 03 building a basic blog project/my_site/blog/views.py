from turtle import pos
from django.shortcuts import render
from datetime import date


all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpeg',
        'author': 'Saddam',
        'date': date(2021, 7, 21),
        'title': 'Mountain Hiking',
        'excerpt': "There's nothing like the view you get when hiking in the mountains! And i wasn't prepared for what happened whilst I was enjoying the view!",
        'content': '''
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sit, unde! Laborum eos minus qui animi autem suscipit perspiciatis et temporibus veritatis optio explicabo, rerum laboriosam debitis, iure distinctio! Nisi, sapiente?

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sit, unde! Laborum eos minus qui animi autem suscipit perspiciatis et temporibus veritatis optio explicabo, rerum laboriosam debitis, iure distinctio! Nisi, sapiente?

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sit, unde! Laborum eos minus qui animi autem suscipit perspiciatis et temporibus veritatis optio explicabo, rerum laboriosam debitis, iure distinctio! Nisi, sapiente?
        '''
    },
    {
        'slug': 'programming-is-fun',
        'image': 'coding.jpeg',
        'author': 'Saddam',
        'date': date(2022, 3, 10),
        'title': 'Programming is Great!',
        'excerpt': "Did you ever spend hours searching that one error in your code? I'm sure you did! But did you know that you can fix it in just a few minutes? I'm sure you can!",
        'content': '''
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sit, unde! Laborum eos minus qui animi autem suscipit perspiciatis et temporibus veritatis optio explicabo, rerum laboriosam debitis, iure distinctio! Nisi, sapiente?

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sit, unde! Laborum eos minus qui animi autem suscipit perspiciatis et temporibus veritatis optio explicabo, rerum laboriosam debitis, iure distinctio! Nisi, sapiente?

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sit, unde! Laborum eos minus qui animi autem suscipit perspiciatis et temporibus veritatis optio explicabo, rerum laboriosam debitis, iure distinctio! Nisi, sapiente?
        '''
    },
    {
        'slug': 'into-the-woods',
        'image': 'woods.jpeg',
        'author': 'Saddam',
        'date': date(2020, 8, 5),
        'title': "Nature At Its Best",
        'excerpt': "Nature is Amazing! The amount of trees and flowers is amazing! I'm sure you'll love the view of the woods!",
        'content': '''
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sit, unde! Laborum eos minus qui animi autem suscipit perspiciatis et temporibus veritatis optio explicabo, rerum laboriosam debitis, iure distinctio! Nisi, sapiente?

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sit, unde! Laborum eos minus qui animi autem suscipit perspiciatis et temporibus veritatis optio explicabo, rerum laboriosam debitis, iure distinctio! Nisi, sapiente?

            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sit, unde! Laborum eos minus qui animi autem suscipit perspiciatis et temporibus veritatis optio explicabo, rerum laboriosam debitis, iure distinctio! Nisi, sapiente?
        '''
    }
]


def get_date(post):
    return post['date']


# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts(request):
    return render(request, 'blog/all-posts.html', {'all_posts': all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {'post': identified_post})