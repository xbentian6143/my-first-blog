
from django import template 
import sys
sys.path.append('../')
from post.models import Good, Sympathy,Idea


register = template.Library()
 
@register.filter(name="goods_count")
def goods_count(idea):
    goods_count = Good.objects.filter(target = idea).count()
    return goods_count


@register.filter(name="sympathys_count")
def sympathys_count(post):
    sympathys_count = Sympathy.objects.filter(target = post).count()
    return sympathys_count


@register.filter(name="ideas_count")
def ideas_count(post):  
    ideas_count = Idea.objects.filter(target = post).count()
    return ideas_count
    