from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Photo


class HomePageView(ListView):
    """Displays a grid of all photos on the homepage, ordered by most recent."""
    model = Photo
    template_name = 'gallery/home.html'
    context_object_name = 'photos'
    ordering = ['-uploaded_at']


class PhotoDetailView(DetailView):
    """Displays a single photo with navigation to the next/previous photo."""
    model = Photo
    template_name = 'gallery/photo_detail.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        """Adds the next and previous photos to the context."""
        context = super().get_context_data(**kwargs)
        photo = self.get_object()

        # Find the previous photo (newer upload date)
        context['previous_photo'] = Photo.objects.filter(uploaded_at__gt=photo.uploaded_at).order_by('uploaded_at').first()

        # Find the next photo (older upload date)
        context['next_photo'] = Photo.objects.filter(uploaded_at__lt=photo.uploaded_at).order_by('-uploaded_at').first()
        return context


def about(request):
    """Renders the static 'About Me' page."""
    return render(request, 'gallery/about.html')



photo = Photo.objects.last()
print(photo.image.url)
