import uuid

from django.db import models

from .utils import generate_random_code


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.choice_text}'


class Quiz(models.Model):
    link = models.CharField(max_length=200, unique=True) 
    creator = models.CharField(max_length=255)
    questions = models.JSONField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.creator} - {self.link}'
    
    def save(self, *args, **kwargs) -> None:
        if self.link:
            super().save(*args, **kwargs)
        else:
            self._generate_link(*args, **kwargs)

    def _generate_link(self, *args, **kwargs):
        """
        Try to generate a unique short link first (9 alphabets only)
        but if all short codes have been exausted already then 
        fallback to uuid 
        """
        link_generated = False

        for _ in range(5):
            self.link = generate_random_code()
            try:
                super().save(*args, **kwargs)
                link_generated = True
            except Exception:
                continue
            else:
                break
    
        if not link_generated:
            self.link = str(uuid.uuid4())
            super().save(*args, **kwargs) 
