# written for python2.7
# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase
from ansible.executor.task_result import TaskResult


DOCUMENTATION = '''
    callback: azdevopslog
    type: aggregate
    short_description: Simple callback for group detail log on Azure devops
    description:
        Simple callback using log formatter in Azure Devops
    '''

class CallbackModule(CallbackBase):

    '''
    Callback Azure devops log formatter
    '''

    CALLBACK_VERSION = 1.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'azdevopslog'

    def __init__(self, *args, **kwargs):
        super(CallbackModule, self).__init__()

    def v2_playbook_on_task_start(self, task, is_conditional):
        print('##[group]Beginning of a group')

    def v2_on_any(self, *args, **kwargs):
        if type(args[0]) == TaskResult : 
            print('##[endgroup]')
