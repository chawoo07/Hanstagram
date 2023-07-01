from django.db import models


# Create your models here.

# Feed
class Feed(models.Model):
    content = models.TextField()        #内容
    image = models.TextField()          # フィードイメージ
    profile_image = models.TextField()  # プロフィール写真
    user_id = models.TextField()        # 書いた人
    like_count = models.IntegerField()  # いいね！数
