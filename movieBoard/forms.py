from django.forms import ModelForm
from django import forms
from movieBoard.models import movie, review
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)

class reviewForm(ModelForm):
    class Meta:
        model = review
        fields = ['point', 'comment', 'movie']
        labels = {
            'point': _('点数'),
            'comment': _('コメント'),
        }
        widgets = {
            'movie': forms.HiddenInput(),
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)
        }
        help_texts = {
            'point': _('点数を入力してください'),
            'comment': _('コメントを入力してください'),
        }


class movieForm(ModelForm):
    class Meta:
        model = movie
        fields = ['name', 'kind', 'actor', 'explain', 'address']
        labels = {
            'name': _('作品'),
            'kind': _('種類'),
            'actor': _('俳優'),
            'explain': _('説明'),
            'address': _('url'),
        }
        help_texts = {
            'name': _('作品名を入力してください。'),
            'kind': _('種類を入力してください。'),
            'actor': _('俳優を入力してください。'),
            'explain': _('説明を入力してください。'),
            'address': _('urlを入力してください。'),
        }
        error_messages = {
            'name': {
                'max_length': _("作品名がながいです。"),
            },
            'explain': {
                'max_length': _("説明がながいです。"),
            },
            'address': {
                'max_length': _("urlがながいです。"),
            },
        }
