from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .responses import bad_request, created


class SRSRetrieveMixin(RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        original_response = super().retrieve(request, *args, **kwargs)
        final_response = {
            'code' : 200,
            'status' : 'OK',
            'message' : 'Success',
            self.listing_name: original_response.data
        }
        return Response(final_response)


class SRSCreateMixin(CreateModelMixin):
    """This makes the responses of create generic views
    compliant to the SRS document we agreed on before"""
    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
        except ValidationError as e:
            response = e
        if response.status_code == 201:
            if "id" in response.data:
                return Response(created(response.data['id']), status=response.status_code)
            else:
                return Response(created(), status=response.status_code)
        elif response.status_code == 400:
            fields = dict(response.detail)
            final_response = bad_request(fields)
            return Response(final_response, status=response.status_code)


class SRSListMixin(ListModelMixin):
    def list(self, request, *args, **kwargs):
        original_response = super().list(request, *args, **kwargs)
        results = original_response.data.pop('results')
        final_response = {
            'code' : 200,
            'status' : 'OK',
            'message' : {
                'numFound' : len(results),
                'numTotal' : original_response.data.pop('count'),
                'nextURL' : original_response.data.pop('next'),
                'prevURL' : original_response.data.pop('previous'),
                self.listing_name : results
            }

        }
        return Response(final_response, status=original_response.status_code)


class SRSUpdateMixin(UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        orignial_response = super().update(request, *args, **kwargs)
        final_response = {
            'code' : 200,
            'status' : 'OK',
            'message' : 'Success',
            self.listing_name : orignial_response.data
        }
        return Response(final_response, status=orignial_response.status_code)

