# models are creates in django for database structure to store data in database
# for this we import models from djngo
from django.db import models

# uuid provides unique id to different user for there session token
import uuid

# database for user model is created consisting of name email and various fields
class UserModel(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

# database for post model is created consisting user as foreign key and various fields
# foreign key links on field of another database to existing databse
class PostModel(models.Model):
    user = models.ForeignKey(UserModel)
    image = models.FileField(upload_to='user_images')
    image_url = models.CharField(max_length=255)
    caption = models.CharField(max_length=240)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    has_liked = False

    @property
    def like_count(self):
        return len(LikeModel.objects.filter(post=self))

    #   @  property allows to use function as a property
    @property
    def comments(self):
        return CommentModel.objects.filter(post=self).order_by('-created_on')

# database for like model is created consisting of various fields used to store value to user who liked the post
class LikeModel(models.Model):
    user = models.ForeignKey(UserModel)
    post = models.ForeignKey(PostModel)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

# database for comment model is created consisting of various fields used to store value to user who commented on the post
class CommentModel(models.Model):
    user= models.ForeignKey(UserModel)
    # this odel has used post as foreign keyuser = models.ForeignKey(UserModel)
    post = models.ForeignKey(PostModel)
    comment_text = models.CharField(max_length=555)
    dots = models.CharField(max_length=555)
    # auto_add_now gives time at which comment is created
    #auto_now gives time on which comment has been updated
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

# this class has been created to store the session toked providd to the user in databse
class SessionToken(models.Model):
    user = models.ForeignKey(UserModel)
    session_token = models.CharField(max_length=255)
    last_request_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    # this will create session token which uses uuid which provide unique session token
    def create_token(self):
        self.session_token = uuid.uuid4()
