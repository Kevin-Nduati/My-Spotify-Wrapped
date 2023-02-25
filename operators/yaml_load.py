import yaml


def yaml_loader():
    config = yaml.safe_load(open("/opt/airflow/operators/config.yml"))
    return config