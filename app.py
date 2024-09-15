#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_stages.cdk_stages_stack import CdkStagesStack
from my_pipeline.my_pipeline_stack import MyPipelineStack

app = cdk.App()

MyPipelineStack(app, "MyPipelineStack",
    env=cdk.Environment(account="000000000000", region="eu-west-1")
)

app.synth()
