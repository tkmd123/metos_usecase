
**AWS EKS security groups allow incoming traffic only on TCP port 443**
- Use case: AWS EKS security groups allow incoming traffic only on TCP port 443
- Sheet Name:
- Row ticket:
- Ticket link:
- Test case: /remediation/test/route/test_aws_remediation_eks.py
- ansible-playbook sg_allow_incoming_tcp_443.yml --extra-vars '{"aws_access_key":"AKIAVEAKLD35OJPCT2LX","aws_secret_key":"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","aws_region":"ap-southeast-1","vpc_id":"vpc-012c931361a99622c","group_name":"eks-cluster-sg-homtech-1093157852"}'

**Envelope encryption for EKS Kubernetes Secrets is enabled using Amazon KMS.**
- Use case: Envelope encryption for EKS Kubernetes Secrets is enabled using Amazon KMS.
- Sheet Name:
- Row ticket:
- Ticket link:
- Test case: /remediation/test/route/test_aws_remediation_eks.py
- ansible-playbook eks_enable_kms_key.yml --extra-vars '{"aws_access_key":"AKIAVEAKLD35OJPCT2LX","aws_secret_key":"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","aws_region":"ap-southeast-1","aws_alias":"eks_key","aws_key_id":"72a201a9-32f1-4b06-a02b-0b9f37a69108"}'
