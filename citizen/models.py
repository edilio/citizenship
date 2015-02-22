from django.db import models


class Category(models.Model):
    index = models.PositiveSmallIntegerField(db_index=True)
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['index']

    def __unicode__(self):
        return self.name


class Question(models.Model):
    index = models.PositiveSmallIntegerField(db_index=True)
    category = models.ForeignKey(Category)
    question = models.CharField(max_length=250)

    class Meta:
        ordering = ['category__index', 'index']

    @property
    def answers(self):
        result = []
        for answer in self.answer_set.all():
            result.append(answer.answer)
        return '='.join(result)

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.TextField()

    def __unicode__(self):
        return 'answer{}'.format(self.id)