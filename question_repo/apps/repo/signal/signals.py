"""
自定义信号
"""
import django.dispatch

mysignal = django.dispatch.Signal(providing_args=["arg1","arg2"])

# 内置的信号会自动触发，自定义信号不可以。



