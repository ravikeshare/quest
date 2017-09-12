from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden, HttpResponse
from django.core.exceptions import PermissionDenied
from quest.tenant.models import Tenant


class TenantMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        key = view_kwargs.get('key', None)
        if '/qa/' in request.path:
            print("key ", key)
            if key:
                try:
                    tenant = Tenant.objects.get(api_key=key)
                    if tenant.is_access_allowed():
                        tenant.update_access_count()
                        print("tenant.remaining_access_count ", tenant.remaining_access_count)

                        return None
                    else:
                        print("tenant access is restricted for 10 seconds")
                        raise PermissionDenied
                except Tenant.DoesNotExist:
                    raise PermissionDenied
            return PermissionDenied
        return None
