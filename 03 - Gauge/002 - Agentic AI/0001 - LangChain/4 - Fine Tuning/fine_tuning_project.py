### Install the client library
"""

!pip install -q google-generativeai

"""### Import libraries"""

import google.generativeai as genai

from google.colab import userdata
genai.configure(api_key=userdata.get('GOOGLE_API_KEY'))

"""You can check you existing tuned models with the `genai.list_tuned_model` method."""

for i, m in zip(range(5), genai.list_tuned_models()):
  print(m.name)

"""## Create tuned model

To create a tuned model, you need to pass your dataset to the model in the `genai.create_tuned_model` method. You can do this be directly defining the input and output values in the call or importing from a file into a dataframe to pass to the method.

For this example, you will tune a model to generate the next number in the sequence. For example, if the input is `1`, the model should output `2`. If the input is `one hundred`, the output should be `one hundred one`.
"""

base_model = [
    m for m in genai.list_models()
    if "createTunedModel" in m.supported_generation_methods and
    "flash" in m.name][0]
base_model

import random

name = f'generate-num-{random.randint(0,10000)}'
operation = genai.create_tuned_model(
    # You can use a tuned model here too. Set `source_model="tunedModels/..."`
    source_model=base_model.name,
    training_data=[
        {
             'text_input': '1',
             'output': '2',
        },{
             'text_input': '3',
             'output': '4',
        },{
             'text_input': '-3',
             'output': '-2',
        },{
             'text_input': 'twenty two',
             'output': 'twenty three',
        },{
             'text_input': 'two hundred',
             'output': 'two hundred one',
        },{
             'text_input': 'ninety nine',
             'output': 'one hundred',
        },{
             'text_input': '8',
             'output': '9',
        },{
             'text_input': '-98',
             'output': '-97',
        },{
             'text_input': '1,000',
             'output': '1,001',
        },{
             'text_input': '10,100,000',
             'output': '10,100,001',
        },{
             'text_input': 'thirteen',
             'output': 'fourteen',
        },{
             'text_input': 'eighty',
             'output': 'eighty one',
        },{
             'text_input': 'one',
             'output': 'two',
        },{
             'text_input': 'three',
             'output': 'four',
        },{
             'text_input': 'seven',
             'output': 'eight',
        }
    ],
    id = name,
    epoch_count = 100,
    batch_size=4,
    learning_rate=0.001,
)

"""Your tuned model is immediately added to the list of tuned models, but its status is set to "creating" while the model is tuned."""

model = genai.get_tuned_model(f'tunedModels/{name}')

model

model.state

"""### Check tuning progress

Use `metadata` to check the state:
"""

operation.metadata

"""Wait for the training to finish using `operation.result()`, or `operation.wait_bar()`"""

import time

for status in operation.wait_bar():
  time.sleep(30)

"""You can cancel your tuning job any time using the `cancel()` method. Uncomment the line below and run the code cell to cancel your job before it finishes."""

# operation.cancel()

"""Once the tuning is complete, you can view the loss curve from the tuning results. The [loss curve](https://ai.google.dev/gemini-api/docs/model-tuning#recommended_configurations) shows how much the model's predictions deviate from the ideal outputs."""

import pandas as pd
import seaborn as sns

model = operation.result()

snapshots = pd.DataFrame(model.tuning_task.snapshots)

sns.lineplot(data=snapshots, x = 'epoch', y='mean_loss')

"""## Evaluate your model

You can use the `genai.generate_content` method and specify the name of your model to test your model performance.
"""

model = genai.GenerativeModel(model_name=f'tunedModels/{name}')

result = model.generate_content('55')
result.text

result = model.generate_content('123455')
result.text

result = model.generate_content('four')
result.text

result = model.generate_content('quatre') # French 4
result.text                               # French 5 is "cinq"

result = model.generate_content('III')    # Roman numeral 3
result.text                               # Roman numeral 4 is IV

result = model.generate_content('七')  # Japanese 7
result.text                            # Japanese 8 is 八!

"""It really seems to have picked up the task despite the limited examples, but "next" is a simple concept, see the [tuning guide](https://ai.google.dev/gemini-api/docs/model-tuning) for more guidance on improving performance.

## Update the description

You can update the description of your tuned model any time using the `genai.update_tuned_model` method.
"""

genai.update_tuned_model(f'tunedModels/{name}', {"description":"This is my model."});

model = genai.get_tuned_model(f'tunedModels/{name}')

model.description

"""## Delete the model

You can clean up your tuned model list by deleting models you no longer need. Use the `genai.delete_tuned_model` method to delete a model. If you canceled any tuning jobs, you may want to delete those as their performance may be unpredictable.
"""

genai.delete_tuned_model(f'tunedModels/{name}')

"""The model no longer exists:"""

try:
  m = genai.get_tuned_model(f'tunedModels/{name}')
  print(m)
except Exception as e:
  print(f"{type(e)}: {e}")

"""### The End..."""