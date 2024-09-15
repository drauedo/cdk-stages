import aws_cdk as cdk
from constructs import Construct
from cdk_stages.cdk_stages_stack import  CdkStagesStack

class MyPipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        sqs = CdkStagesStack(self, "SqsStack")