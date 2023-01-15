from django.views.generic import TemplateView


# class Role(models.model):
#    name = models.CharField(...)

# class Person(models.model):
#     user = models.OneToOne(User, ...)
#     roles = models.ManyToMany(Role, related_name="persons", ..)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        # this code does nothing right now, add result['xxyy'] = blabla
        # to pass xxyy to template
        return result


