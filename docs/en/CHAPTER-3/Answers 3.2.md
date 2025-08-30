# Answers 3.2

## Theory
1. Kubeflow Pipelines automate ML workflows, providing reproducibility and saving time through efficient management of complex pipelines.
2. The `dsl` module provides decorators and classes for defining components and pipeline structure, while the `compiler` is responsible for compiling the pipeline into a format executable by the Kubeflow engine.
3. `FutureWarning` messages can be selectively suppressed to improve log readability; at the same time, it is important to keep track of documentation changes and update the code accordingly.
4. Clearly defined interfaces and component reusability simplify integration, increasing modularity and overall system efficiency.
5. The `@dsl.component` decorator marks a function as a pipeline component, which is an isolated, reusable step within the workflow.
6. Invoking a component returns a `PipelineTask` object, which represents a runtime instance of the pipeline step and is used to pass data between components.
7. A component’s output is passed via the `.output` attribute of the `PipelineTask` object.
8. Using named arguments improves code clarity and helps prevent errors, especially when working with many input parameters.
9. When chaining components in a pipeline, you must pass one component’s `.output` as the input to another to ensure a correct data flow.
10. A pipeline is declared with the `@dsl.pipeline` decorator and is responsible for orchestrating components. Important aspects include the execution environment and proper handling of outputs.
11. Pipeline compilation is the process of converting its Python definition into a YAML file, which can then be uploaded and run in the target Kubeflow environment.
12. Reusing ready‑made pipelines (e.g., PEFT for PaLM 2) significantly speeds up development and helps maintain best practices.
13. Model versioning is critical for MLOps, ensuring reproducibility and auditability. For example, you can add the date and time to the model name.
14. Pipeline arguments set input data and configuration for fine‑tuning, which is crucial for correct execution.
15. Automation and orchestration in Kubeflow improve efficiency and scalability, but require careful planning and a deep understanding of components and data flow.

## Practice
Solutions for the tasks:

### 1. Setting up the Kubeflow Pipelines SDK

```python
# Import the required modules from the Kubeflow Pipelines SDK
from kfp import dsl, compiler

# Suppress FutureWarning messages from the Kubeflow Pipelines SDK
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module='kfp.*')
```

This script imports `dsl` and `compiler`, and suppresses `FutureWarning` messages from `kfp.*` modules.

### 2. Defining a simple pipeline component

```python
from kfp import dsl

# Define a simple component that adds two numbers
@dsl.component
def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2
```

The component function `add_numbers`, marked with the `@dsl.component` decorator, accepts two integers and returns their sum.

### 3. Suppressing specific warnings

```python
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
```

This script suppresses `DeprecationWarning` for all modules.

### 4. Linking components in a pipeline

```python
from kfp import dsl

# Component that generates a fixed number
@dsl.component
def generate_number() -> int:
    return 42

# Component that doubles the input number
@dsl.component
def double_number(input_number: int) -> int:
    return input_number * 2

# Define a pipeline that connects two components
@dsl.pipeline(
    name="Number doubling pipeline",
    description="A pipeline that generates a number and doubles it."
)
def number_doubling_pipeline():
    # Step 1: Generate a number
    generated_number_task = generate_number()

    # Step 2: Double the generated number
    double_number_task = double_number(input_number=generated_number_task.output)
```

The pipeline consists of two components: `generate_number`, which generates a fixed number, and `double_number`, which doubles the input. The connection is made by passing the first component’s `.output` as the input to the second.

### 5. Compiling and preparing the pipeline for execution

```python
from kfp import compiler

# Assume the pipeline definition is named number_doubling_pipeline
pipeline_func = number_doubling_pipeline

# Compile the pipeline
compiler.Compiler().compile(
    pipeline_func=pipeline_func,
    package_path='number_doubling_pipeline.yaml'
)
```

The pipeline is compiled into the `number_doubling_pipeline.yaml` file, which can be uploaded and run in the Kubeflow environment.

### 6. Working with `PipelineTask` objects

```python
# This is a hypothetical function that cannot be executed as‑is. It is intended to illustrate the concept.
def handle_pipeline_task():
    # Hypothetical call to a component function named my_component
    # In a real scenario, this should occur inside a pipeline function
    task = my_component(param1="value")

    # Access the component’s output
    # This line is illustrative and typically used to pass outputs between components in a pipeline
    output = task.output

    print("Accessing the component output:", output)

# Note: In real usage, my_component would be defined as a Kubeflow Pipeline component,
# and task manipulations should occur within the context of a pipeline function.
```

The example shows that invoking a component returns a `PipelineTask` object, and its result is accessed via `task.output`. In practice, such objects are manipulated inside a pipeline function.

### 7. Handling errors in pipeline definitions

```python
from kfp import dsl

# Incorrect pipeline definition
@dsl.pipeline(
    name='Incorrect Pipeline',
    description='An example that attempts to return a PipelineTask object directly.'
)
def incorrect_pipeline_example():
    @dsl.component
    def generate_number() -> int:
        return 42

    generated_number_task = generate_number()
    # Incorrect attempt to return a PipelineTask object directly
    return generated_number_task  # This will cause an error

# Correct pipeline definition
@dsl.pipeline(
    name='Correct Pipeline',
    description='A corrected example that does not attempt to return a PipelineTask object.'
)
def correct_pipeline_example():
    @dsl.component
    def generate_number() -> int:
        return 42

    generated_number_task = generate_number()
    # Correct approach: do not attempt to return a PipelineTask directly from a pipeline function.
    # A pipeline function should not return anything.

# Explanation: a pipeline function orchestrates steps and data flow, but does not return data directly.
# Attempting to return a PipelineTask from a pipeline function is incorrect, because the pipeline definition
# should describe component structure and dependencies, not process data directly.
# The corrected version removes the return statement, which matches the expected behavior of pipeline functions.
```

### 8. Automating data preparation for model training

```python
import json

# Simulated data preparation for model training
def preprocess_data(input_file_path, output_file_path):
    # Read data from a JSON file
    with open(input_file_path, 'r') as infile:
        data = json.load(infile)

    # Perform a simple transformation: filter data
    # For illustration, assume we only need items meeting a certain condition
    # Example: filter items where the value of "useful" is True
    filtered_data = [item for item in data if item.get("useful", False)]

    # Save the transformed data to another JSON file
    with open(output_file_path, 'w') as outfile:
        json.dump(filtered_data, outfile, indent=4)

# Example usage
preprocess_data('input_data.json', 'processed_data.json')

# Note: This script assumes the file 'input_data.json' exists in the current directory
# and will save processed data to 'processed_data.json'.
# In a real scenario, paths and transformation logic should be adjusted to your requirements.
```

This script demonstrates a simple data preparation process: reading data from a JSON file, transforming it (filtering by a condition), and saving the processed data to another JSON file. This type of task can be encapsulated in a Kubeflow Pipeline component to automate data preparation steps in ML training workflows.

### 9. Implementing model versioning in a pipeline

```python
from datetime import datetime

def generate_model_name(base_model_name: str) -> str:
    # Generate a timestamp in the format "YYYYMMDD-HHMMSS"
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    # Append the timestamp to the base model name to create a unique name
    model_name = f"{base_model_name}-{timestamp}"
    return model_name

# Example usage
base_model_name = "my_model"
model_name = generate_model_name(base_model_name)
print("Generated model name:", model_name)

# This function generates a unique model name by appending the current date and time to the base model name.
# This practice helps with model versioning, making it easier to track and manage different model versions in ML operations.
```

### 10. Parameterizing and executing a Kubeflow pipeline

For the purpose of this task, assume we are working in an environment with access to a Kubeflow Pipeline execution API. Since execution details vary by platform and API version, the following script is a hypothetical example based on common patterns.

```python
# Assume the necessary imports and configuration for interacting with the execution environment are present

def submit_pipeline_execution(compiled_pipeline_path: str, pipeline_arguments: dict):
    # Placeholder for the API/SDK method to submit a pipeline for execution
    # In a real scenario, this would use the Kubeflow Pipelines SDK or a cloud provider SDK
    # For example, using the Kubeflow Pipelines SDK or a cloud service like Google Cloud AI Platform Pipelines

    # Assume a function `submit_pipeline_job` exists and can be used to submit
    # This function would be part of the SDK or the environment’s API
    submit_pipeline_job(compiled_pipeline_path, pipeline_arguments)

# Example pipeline arguments
pipeline_arguments = {
    "recipient_name": "Alice"
}

# Path to the compiled Kubeflow pipeline YAML file
compiled_pipeline_path = "path_to_compiled_pipeline.yaml"

# Submit the pipeline for execution
submit_pipeline_execution(compiled_pipeline_path, pipeline_arguments)

# Note: This example assumes a `submit_pipeline_job` function exists, which will be specific
# to the environment’s API or SDK. In a real implementation, replace this placeholder
# with actual code that interacts with the Kubeflow Pipelines API or a managed service API, such as Google Cloud AI Platform.
```

This script describes how to parameterize and submit a compiled Kubeflow pipeline for execution, assuming an appropriate API or SDK method is available (`submit_pipeline_job` in this hypothetical example). The actual submission method depends on your execution environment or cloud provider.

