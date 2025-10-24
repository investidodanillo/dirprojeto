# core/threadlocal.py
import threading

_thread_locals = threading.local()

def set_current_company(company):
    """company: instance or None"""
    _thread_locals.current_company = company

def get_current_company():
    return getattr(_thread_locals, "current_company", None)

def set_current_company_id(company_id):
    _thread_locals.current_company_id = company_id

def get_current_company_id():
    return getattr(_thread_locals, "current_company_id", None)


