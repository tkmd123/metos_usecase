import os
from unittest import TestCase
from json import loads, dumps
from jsonpath_ng import parse


class TestCloudSql(TestCase):
    def setUp(self):
        fp = open(os.getcwd() + "/test/data/test_aws_eks_resource.json", "r")
        content = fp.read()
        fp.close()
        self.resources = loads(content)

    def test_eks_security_groups_allow_incoming_traffic(self):
        """
        EKS security groups allow incoming traffic only on TCP port 443
        """
        rs_sg = [match.value for match in parse('cluster[*].self.source_data.resourcesVpcConfig.clusterSecurityGroupId').find(self.resources)]
        rg_sg_id = len(set(rs_sg)) == 1 and set(rs_sg).pop()
        sg = parse('network[*].self[*].source_data[*].security_group[*]').find(self.resources)
        sg_rule = [match.value.get('IpPermissions') for match in sg if 'sg-02e101c951f087ace' in match.value.get('GroupId')]
        IpPermissions = sg_rule.pop()
        alow_tcp_443 = [match for match in IpPermissions if match.get('FromPort','') == 443 and  match.get('ToPort','') == 443 and match.get('IpProtocol','') == 'tcp']
        flag = len(alow_tcp_443) >= 1
        self.assertEqual(True, flag, msg="EKS security groups allow incoming traffic only on TCP port 443")

    def test_eks_encryption_is_enabled(self):
        """
        Envelope encryption for EKS Kubernetes Secrets is enabled using Amazon KMS
        """
        encryptionConfig = [match.value for match in parse('cluster[*].self.source_data.encryptionConfig').find(self.resources)]
        flag = len(encryptionConfig) >= 1
        self.assertEqual(True, flag, msg="Envelope encryption for EKS Kubernetes Secrets is enabled using Amazon KMS")    
