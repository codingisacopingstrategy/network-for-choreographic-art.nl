from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from network_for_choreographic_art.petition.models import Vote
from network_for_choreographic_art.texts.models import Text, Paragraph

def text(request, slug):
    text = get_object_or_404(Text, slug=slug)
    paragraphs = Paragraph.objects.filter(text__slug=slug)
    return render_to_response('text.html',{'slug': 'text_' + slug, 'text' : text, 'paragraphs' : paragraphs},context_instance=RequestContext(request))

def proposal(request):
    text = Paragraph.objects.filter(text__slug='proposal')
    petition = Vote.objects.all().order_by('-pub_date')
    return render_to_response('text2.html',{'slug': 'text', 'text' : text, 'petition': petition, 'count' : len(petition)},context_instance=RequestContext(request))
