import os
import sys
from synchronizers.new_base.SyncInstanceUsingAnsible import SyncInstanceUsingAnsible
from synchronizers.new_base.modelaccessor import *
from xos.logger import Logger, logging

parentdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, parentdir)

logger = Logger(level=logging.INFO)

class SyncNginxServiceInstance(SyncInstanceUsingAnsible):

    provides = [NginxServiceInstance]

    observes = NginxServiceInstance

    requested_interval = 0

    template_name = "nginxserviceinstance_playbook.yaml"

    service_key_name = "/opt/xos/synchronizers/nginxservice/nginxservice_private_key"

    def __init__(self, *args, **kwargs):
        super(SyncNginxServiceInstance, self).__init__(*args, **kwargs)

    def get_nginxservice(self, o):
        if not o.owner:
            return None

        nginxservice = NginxService.objects.filter(id=o.owner.id)

        if not nginxservice:
            return None

        return nginxservice[0]

    # Gets the attributes that are used by the Ansible template but are not
    # part of the set of default attributes.
    def get_extra_attributes(self, o):
        fields = {}
        fields['tenant_message'] = o.tenant_message
        nginxservice = self.get_nginxservice(o)
        fields['service_message'] = nginxservice.service_message
        return fields

    def delete_record(self, port):
        # Nothing needs to be done to delete an nginxservice; it goes away
        # when the instance holding the nginxservice is deleted.
        pass
