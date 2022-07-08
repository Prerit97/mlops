start_pipeline = pipeline_jobs.PipelineJob(
    display_name="winequality-pipeline",
    template_path="gs://mlops-bucket-wineqaulity/ml_winequality.json",
    enable_caching=True,
    location="europe-west1",
)

start_pipeline.run()
