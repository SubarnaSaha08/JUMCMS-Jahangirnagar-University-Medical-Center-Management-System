# blogs/test_forms.py
from django.test import TestCase
from blogs.forms import BlogForm
from blogs.models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogFormTests(TestCase):
    def setUp(self):
        # Create a user to associate with the blog post
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_blog_form_valid(self):
        form_data = {
            'title': 'Test Blog Title',
            'content': 'This is a test blog content.',
            'image': None,  # Assuming you are not uploading an image in this test
            'tags': 'test, blog, django'
        }
        form = BlogForm(data=form_data)

        self.assertTrue(form.is_valid())
        blog = form.save(commit=False)  # Create a Blog instance without saving to the database
        blog.author = self.user  # Set the author
        blog.save()  # Save the blog instance to the database

        # Verify the blog was created
        self.assertEqual(Blog.objects.count(), 1)
        self.assertEqual(Blog.objects.first().title, 'Test Blog Title')

    def test_blog_form_invalid_without_title(self):
        form_data = {
            'title': '',  # Title is required
            'content': 'This is a test blog content.',
            'image': None,
            'tags': 'test, blog, django'
        }
        form = BlogForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)  # Check that 'title' is in the form errors

    def test_blog_form_invalid_without_content(self):
        form_data = {
            'title': 'Test Blog Title',
            'content': '',  # Content is required
            'image': None,
            'tags': 'test, blog, django'
        }
        form = BlogForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)  # Check that 'content' is in the form errors
