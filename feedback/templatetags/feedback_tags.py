from itertools import chain
from operator import attrgetter
from django.template import Library, Node

from feedback.models import Feedback, AnonymousFeedback

register = Library()

@register.tag
def get_feedback(parser, token):
    """
    {% get_feedback %}
    """
    return FeedbackNode()
    
class FeedbackNode(Node):
    def render(self, context):
        context['feedback'] = sorted(chain(Feedback.objects.all(), AnonymousFeedback.objects.all()),
                                    key=attrgetter('time'), reverse=True)
        return ''