from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save

# 请求完成后，打印一个日志
@receiver(request_finished)
def all_log(sender,**kwargs):
    print(sender,kwargs)
    print("使用信号记日志")

# 当创建一条记录MailLog之后，会自动执行发送邮件