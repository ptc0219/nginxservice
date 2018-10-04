from synchronizers.new_base.modelaccessor import *
from synchronizers.new_base.model_policies.model_policy_tenantwithcontainer import TenantWithContainerPolicy

class NginxServiceInstancePolicy(TenantWithContainerPolicy):
    model_name = "NginxServiceInstance"
