# core/managers.py
# core/managers.py
from django.db import models
from core.threadlocal import get_current_company_id

class TenantQuerySet(models.QuerySet):
    def _tenant_filter_kwargs(self):
        company_id = get_current_company_id()
        if company_id is None:
            return {}
        return {"company_id": company_id}

    def all(self):
        # override all() to apply tenant filter if set
        kw = self._tenant_filter_kwargs()
        if kw:
            return super().filter(**kw)
        return super().all()

    def filter(self, *args, **kwargs):
        # apply tenant filter unless explicitly passed company_id
        if "company_id" not in kwargs and "company" not in kwargs:
            kw = self._tenant_filter_kwargs()
            if kw:
                kwargs.update(kw)
        return super().filter(*args, **kwargs)

    def get(self, *args, **kwargs):
        if "company_id" not in kwargs and "company" not in kwargs:
            kw = self._tenant_filter_kwargs()
            if kw:
                kwargs.update(kw)
        return super().get(*args, **kwargs)

class TenantManager(models.Manager):
    def get_queryset(self):
        qs = TenantQuerySet(self.model, using=self._db)
        # If tenant is set, apply filter
        company_id = get_current_company_id()
        if company_id is not None:
            return qs.filter(company_id=company_id)
        return qs
