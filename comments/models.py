from django.contrib.comments.models import Comment
from mptt.models import MPTTModel, TreeForeignKey

from django.contrib.humanize.templatetags.humanize import naturalday


class MPTTComment(MPTTModel, Comment):
    """ Threaded comments - Add support for the parent comment store and MPTT traversal"""
    # a link to comment that is being replied, if one exists
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        # comments on one level will be ordered by date of creation
        order_insertion_by = ['submit_date']

    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    @property
    def human_add_date(self):
        """
            Add date in human readable format
        """
        return naturalday(self.submit_date)