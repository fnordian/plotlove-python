import requests

class Measurement:
    def __init__(self, name: str, x_column_name: str, measurementId = None, apiurl="http://plot.love"):
        self.apiurl = apiurl
        self.measurementId = measurementId if measurementId != None else self.create_new_measurement(name, x_column_name)

    def create_new_measurement(self, name: str, x_column_name: str):
        response = requests.post(f'{self.apiurl}/measurement', json={'name': name, 'xColumnName': x_column_name})
        return response.json()["measurementId"]

    def log_measurement(self, data:dict):
        return self.log_measurement_for_id(self.measurementId, data)

    def log_measurement_for_id(self, measurementId: int, data: dict):
        response = requests.post(f'{self.apiurl}/measurement/{measurementId}/datapoint', json=data)

    def plot_url(self):
        return f'{self.apiurl}/?id={self.measurementId}'


    @staticmethod
    def dummy():
        class DummyMeasurement:
            def log_measurement(self, data:dict):
                pass

        return DummyMeasurement()