from django.db import models
from django.core.urlresolvers import reverse
from entities.models import Person, Institution
from idprovider.models import IdProvider


class RepoObject(IdProvider):
    has_title = models.CharField(
        max_length=250, blank=True, verbose_name="acdh:hasTitle",
        help_text="Title or name of Collection."
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="acdh:hasDescription",
        help_text="A verbose description of certain aspects of an entity. \
        This is the most generic property, use more specific sub-properties where applicable."
    )

    class Meta:
        abstract = True


class Collection(RepoObject):
    part_of = models.ForeignKey(
        'Collection', blank=True, null=True, verbose_name="acdh:isPartOf",
        help_text="Indicates A is a part of aggregate B, \
        e. g. elements of a series, items of a collection.", related_name="has_part"
    )
    has_contributor = models.ManyToManyField(
        Person, blank=True, verbose_name="acdh:hasContributor",
        help_text="Agent (person, group, organisation) (B) who was actively involved in \
        creating/curating/editing a Resource, a Collection or in a Project (A).",
        related_name="contributes_to_collection"
    )

    def __str__(self):
        return "{}".format(self.has_title)

    def get_absolute_url(self):
        return reverse('arche:collection_detail', kwargs={'pk': self.id})

    @classmethod
    def get_createview_url(self):
        return reverse('arche:collection_create')

    @classmethod
    def get_listview_url(self):
        return reverse('arche:browse_collections')

    @classmethod
    def get_arche_dump(self):
        return reverse('arche:rdf_collections')

    def get_next(self):
        next = Collection.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Collection.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False


class Project(RepoObject):
    has_principal = models.ManyToManyField(
        Person, blank=True, verbose_name="acdh:hasPrincipalInvestigator",
        help_text="Person officially designated as head of project team or subproject \
        team instrumental in the work necessary to development of the resource.",
        related_name="is_principal"
    )
    has_contributor = models.ManyToManyField(
        Person, blank=True, verbose_name="acdh:hasContributor",
        help_text="Agent (person, group, organisation) (B) who was actively involved in \
        creating/curating/editing a Resource, a Collection or in a Project (A).",
        related_name="contributes_to_project"
    )
    has_start_date = models.DateField(
        blank=True, null=True, verbose_name="acdh:hasStartDate",
        help_text="Indicates the start date of a Project."
    )
    has_end_date = models.DateField(
        blank=True, null=True, verbose_name="acdh:hasEndtDate",
        help_text="Indicates the end date of a Project."
    )
    has_funder = models.ManyToManyField(
        Institution, blank=True, verbose_name="acdh:hasFunder",
        help_text="Organisation (B) which provided funding for the project (A).",
        related_name="is_funding"
    )
    related_collection = models.ManyToManyField(
        Collection, blank=True, verbose_name="acdh:hasRelatedCollection",
        help_text="Indication of a project (B) associated with this resource or collection (A).",
        related_name="has_related_project"
    )

    def __str__(self):
        return "{}".format(self.has_title)

        def get_absolute_url(self):
            return reverse('arche:project_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('arche:project_detail', kwargs={'pk': self.id})

    @classmethod
    def get_createview_url(self):
        return reverse('arche:project_create')

    @classmethod
    def get_listview_url(self):
        return reverse('arche:browse_projects')

    @classmethod
    def get_arche_dump(self):
        return reverse('arche:rdf_projects')

    def get_next(self):
        next = Project.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Project.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False
