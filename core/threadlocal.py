# core/threadlocal.py
import threading

_thread_locals = threading.local()

def set_current_empresa(empresa):
    _thread_locals.empresa = empresa

def get_current_empresa():
    return getattr(_thread_locals, 'empresa', None)