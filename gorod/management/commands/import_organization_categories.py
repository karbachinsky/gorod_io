""" Scripts allows to import organization categories from yaml file """

from django.core.management.base import BaseCommand, CommandError
from gorod.models import OrganizationCategory

import yaml, os.path
from optparse import make_option


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--yaml-file',
            default=False,
            help='Yaml file with organization categories'),
    )

    def handle(self, *args, **options):
        """ Command execution """ 
        yaml_file = options.get('yaml_file','')

        if not os.path.isfile(yaml_file): 
            raise CommandError("Input file '%s' specifyed by --yaml-file option doesn't exist!" % yaml_file)
    
        with open(yaml_file, 'r') as f:
            try:
                data = yaml.load(f)
                self._save_categories(data)
            except yaml.YAMLError, exc:
                if hasattr(exc, 'problem_mark'):
                    mark = exc.problem_mark
                    print "Error position: (%s:%s)" % (mark.line+1, mark.column+1)


    def _save_category(self, title, parent=None):
        """ Save one category """
        category = None
        try:
            category = OrganizationCategory(
                title=title,
                name=title,
                parent=parent if parent else None
            )        
            
            category.save()
        except Exception as e:
            raise CommandError("Failed to save category with title '%s'. Error: %s" % (title, str(e)))

        return category


    def _save_categories(self, categories, parent=None):
        """ Save categories parsed from yaml file """

        if isinstance(categories, str) or isinstance(categories, unicode):
            self._save_category(categories, parent)

        elif isinstance(categories, dict):             
            for category, sub_categories in categories.items():
                cur_parent = self._save_category(category, parent)
                self._save_categories(sub_categories, cur_parent)

        elif isinstance(categories, list):
            for category in categories:
                self._save_categories(category, parent)


