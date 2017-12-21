import rdflib
from django.conf import settings
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, RDFS, ConjunctiveGraph
from rdflib.namespace import DC, FOAF, RDFS
from rdflib.namespace import SKOS
from .models import Place, Institution

project_name = settings.ROOT_URLCONF.split('.')[0]
ARCHE = Namespace('https://vocabs.acdh.oeaw.ac.at/schema#')
ACDH = Namespace('https://id.acdh.oeaw.ac.at/')
GEONAMES = Namespace('http://www.geonames.org/ontology#')
base_url = "https://id.acdh.oeaw.ac.at/{}".format(project_name)


def place_to_arche(itmes):

    """takes queryset of Place objects and returns a ARCHE rdflib.Graph"""

    g = rdflib.Graph()
    for obj in itmes:
        subject = URIRef('/'.join([base_url, 'place', str(obj.id)]))
        if obj.name:
            g.add((subject, ARCHE.hasTitle, Literal(obj.name)))
        if obj.alternative_name:
            for x in obj.alternative_name.all():
                if x.name:
                    g.add((subject, ARCHE.hasAlternativeTitle, Literal(x.name)))
        if obj.geonames_id:
            g.add((subject, ARCHE.hasIdentifier, URIRef(obj.get_geonames_url())))
        if obj.lat:
            g.add((subject, ARCHE.hasLongitude, Literal(obj.lng)))
            g.add((subject, ARCHE.hasLatitude, Literal(obj.lat)))
        if obj.part_of:
            if obj.part_of.geonames_id:
                g.add((
                    subject, GEONAMES.parentFeature,
                    URIRef('/'.join([base_url, 'place', str(obj.part_of.id)]))
                ))
    return g


def inst_to_arche(insitutions):

    """takes queryset of Insititution objects and returns a ARCHE rdflib.Graph"""

    g = rdflib.Graph()
    for obj in insitutions:
        inst = URIRef('/'.join([base_url, 'institution', str(obj.id)]))
        if obj.written_name:
            g.add((inst, ARCHE.hasTitle, Literal(obj.written_name)))
        if obj.alt_names:
            g.add((inst, ARCHE.hasAlternativeTitle, Literal(obj.alt_names)))
        if obj.abbreviation:
            g.add((inst, ARCHE.hasAlternativeTitle, Literal(obj.abbreviation)))
        if obj.parent_institution:
            g.add((
                inst, ARCHE.isMember,
                URIRef('/'.join([
                    base_url, 'institution', str(obj.parent_institution.id)
                ]))
            ))
        if obj.location:
            pl = URIRef('/'.join([base_url, 'place', str(obj.location.id)]))
            loc_g = place_to_arche([obj.location])
            g = g + loc_g
            g.add((inst, ARCHE.hasSpatialCoverage, URIRef(pl)))
        if obj.authority_url:
            g.add((inst, ARCHE.hasIdentifier, URIRef(obj.authority_url)))
    return g


def person_to_arche(itmes):

    """takes queryset of Person objects and returns a ARCHE rdflib.Graph"""

    g = rdflib.Graph()
    for obj in itmes:
        subject = URIRef('/'.join([base_url, 'person', str(obj.id)]))
        if obj.written_name:
            g.add((subject, ARCHE.hasAlternativeTitle, Literal(obj.written_name)))
        if obj.name:
            g.add((subject, ARCHE.hasLastName, Literal(obj.name)))
        if obj.forename:
            g.add((subject, ARCHE.hasFirstName, Literal(obj.forename)))
        if obj.acad_title and obj.acad_title != 'nan':
            g.add((subject, ARCHE.hasPersonalTitle, Literal(obj.acad_title)))
        if obj.belongs_to_institution:
            inst = URIRef(
                '/'.join([base_url, 'institution', str(obj.belongs_to_institution.id)])
            )
            inst_g = inst_to_arche([obj.belongs_to_institution])
            g = g + inst_g
            g.add((subject, ARCHE.isMember, inst))
    return g
