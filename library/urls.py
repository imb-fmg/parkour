from django.conf.urls import url
from library.views import LibraryField, LibraryView


urlpatterns = [
    url(r'^get_library_protocols/$', LibraryField.as_view(), name='get_library_protocols'),
    url(r'^get_library_type/$', LibraryField.as_view(), name='get_library_type'),
    url(r'^get_organisms/$', LibraryField.as_view(), name='get_organisms'),
    url(r'^get_index_types/$', LibraryField.as_view(), name='get_index_types'),
    url(r'^get_index_i7/$', LibraryField.as_view(), name='get_index_i7'),
    url(r'^get_index_i5/$', LibraryField.as_view(), name='get_index_i5'),
    url(r'^get_concentration_methods/$', LibraryField.as_view(), name='get_concentration_methods'),
    url(r'^get_sequencing_run_conditions/$', LibraryField.as_view(), name='get_sequencing_run_conditions'),

    url(r'^get_libraries/$', LibraryView.as_view(), name='get_libraries'),
    url(r'^get_library/$', LibraryView.as_view(), name='get_library'),

    url(r'^save_library/$', LibraryView.as_view(), name='save_library'),
    url(r'^edit_library/$', LibraryView.as_view(), name='edit_library'),
    url(r'^delete_library/$', LibraryView.as_view(), name='delete_library'),
]
