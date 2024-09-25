class FixStatusMixin:
    """
    A mixin that allows to fix the status code of the response.
    """
    fix_status = None

    def finalize_response(self, request, response, *args, **kwargs):
        if self.fix_status is not None:
            response.status_code = self.fix_status
        return super().finalize_response(request, response, *args, **kwargs)
