import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep, ManualApprovalStep
from my_pipeline.my_pipeline_app_stage import MyPipelineAppStage

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline",
                        pipeline_name="MyPipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub("drauedo/cdk-stages", "main"),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        )
                    )
        
        testing_stage = pipeline.add_stage(MyPipelineAppStage(self, "test",
            env=cdk.Environment(account="590184009415", region="us-east-1")))
        
        testing_stage.add_post(ManualApprovalStep('approval'))

        pro_stage = pipeline.add_stage(MyPipelineAppStage(self, "pro",
            env=cdk.Environment(account="590184009415", region="us-east-1")))