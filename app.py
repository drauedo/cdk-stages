#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_stages.cdk_stages_stack import CdkStagesStack
from my_pipeline.my_pipeline_stack import MyPipelineStack

app = cdk.App()

MyPipelineStack(app, "MyPipelineStack",
    env=cdk.Environment(account="590184009415", region="us-east-1")
)

app.synth()
