from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	song_title = models.CharField(max_length = 50)
	artist_name = models.CharField(max_length = 50)
	solo_or_group = models.CharField(max_length = 100)
	genre = models.CharField(max_length = 15)
	language = models.CharField(max_length = 100)
	date_released = models.CharField(max_length = 50)
	
	
	def __str__(self):
 		return(f"{self.song_title} {self.artist_name}")