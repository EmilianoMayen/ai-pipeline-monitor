"""
AI Pipeline Monitor
Pipeline Generator

This module generates simulated pipeline executions for testing
the monitoring engine and AI agent.
"""

from dataclasses import dataclass
from datetime import datetime
import random


@dataclass
class PipelineExecution:
    pipeline_name: str
    workspace: str
    status: str
    duration_seconds: int
    records_processed: int
    error_message: str
    execution_time: datetime


PIPELINES = [
    "Meta_US",
    "Meta_LATAM",
    "GoogleAds_Global",
    "DV360",
    "TikTok_US",
    "TikTok_LATAM",
    "Salesforce",
    "GA4",
    "AmazonAds",
    "CM360"
]

WORKSPACES = [
    "Marketing",
    "Finance",
    "Sales",
    "Analytics",
    "Operations"
]

STATUS = [
    "Completed",
    "Running",
    "Failed",
    "Warning"
]

ERRORS = [
    "",
    "",
    "",
    "",
    "",
    "HTTP 401 Unauthorized",
    "Timeout exceeded",
    "Connection refused",
    "Missing credentials",
    "Source unavailable"
]


def generate_pipeline():

    status = random.choices(
        STATUS,
        weights=[70, 10, 10, 10]
    )[0]

    error = ""

    if status == "Failed":
        error = random.choice(ERRORS[5:])

    return PipelineExecution(
        pipeline_name=random.choice(PIPELINES),
        workspace=random.choice(WORKSPACES),
        status=status,
        duration_seconds=random.randint(20, 400),
        records_processed=random.randint(0, 500000),
        error_message=error,
        execution_time=datetime.now()
    )


def generate_pipelines(quantity=100):

    return [
        generate_pipeline()
        for _ in range(quantity)
    ]


if __name__ == "__main__":

    pipelines = generate_pipelines(10)

    for pipeline in pipelines:
        print(pipeline)


