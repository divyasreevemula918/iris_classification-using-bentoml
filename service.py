import bentoml
import numpy as np

# Load model
model = bentoml.sklearn.load_model("iris_clf:latest")

# Create service
@bentoml.service
class IrisService:

    @bentoml.api
    def predict(self, input_data: list[float]) -> str:
        arr = np.array(input_data).reshape(1, -1)
        prediction = model.predict(arr)[0]
        return str(prediction)