from django.shortcuts import render
from datetime import date
posts=[
    {
        'slug':'hike-in-the-mountains',
        'image':'mountains.jpg',
        'author':'Maximilian',
        'date':date(2023,9,21),
        'title':'Mountain Hiking',
        'excerpt':'There\'s nothing like the views you get while Hiking in the mountains and I wasn\'t even prepared for the view I saw when hiking in the mountain.',
            'content':'''
Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis.
        '''
    }
]
def starting_page(request):
    return render(request,'blog/index.html')
def posts(request):
    return render(request, 'blog/all-posts.html')
def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
