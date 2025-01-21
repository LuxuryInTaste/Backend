from django.http import JsonResponse
from .models import Newsletter

def newsletter_list(request):
    """Fetch all newsletter entries."""
    newsletters = Newsletter.objects.all().order_by('-created_at')
    data = [
        {
            "title": newsletter.title,
            "description": newsletter.description,
            "image": newsletter.image.url if newsletter.image else None,
            "link": newsletter.link,
        }
        for newsletter in newsletters
    ]
    return JsonResponse({"newsletters": data}, safe=False)
