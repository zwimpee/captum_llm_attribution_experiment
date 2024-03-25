# Captum LLM Interpretability Experiment

## Objective
The goal of this experiment is to evaluate the interpretability of the Meditron 7B large language model (LLM) in predicting patient discharge status from clinical notes within the MIMIC dataset. This project aims to provide insights into which features (words or phrases from clinical notes) significantly influence the model's predictions, leveraging Captum for attribution analysis.

## Preparation Phase

### Dataset Access and Selection
We use a subset of the MIMIC-III or MIMIC-IV dataset, focusing on discharge summaries for ICU patients. Access to MIMIC data requires appropriate approvals and compliance with all ethical guidelines.

### Preprocessing
Scripts are provided for de-identification, tokenization, and summarization of clinical notes to prepare the data for model input.

## Experiment Design

### Feature Extraction
Clinical notes are used directly as input to Meditron 7B, aiming to minimize preprocessing steps due to the time constraints of the experiment.

### Model Loading and Configuration
The pre-trained Meditron 7B model is configured for predicting patient discharge status, with dynamic allocation based on available computational resources.

### Interpretability Analysis Setup
We utilize Feature Ablation and Layer Integrated Gradients techniques to analyze the model's decision-making process, providing a granular view of feature influence.

## Execution Phase

### Model Inference
The model predicts discharge status for the selected patient notes, with the process being dynamically adjusted to fit within the experiment's timeframe.

### Interpretability Analysis
Interpretability techniques are applied to understand the influence of different features on the model's predictions, highlighting the impact of specific clinical note components.

## Evaluation and Analysis

### Performance Metrics
The model's performance is evaluated using accuracy, precision, recall, and F1 score to ensure reliability and effectiveness.

### Interpretability Insights
A detailed analysis documents which features significantly affect the model's discharge status predictions, offering valuable insights into the model's decision-making logic.

## Documentation and Review

### Findings Documentation
This section includes comprehensive documentation of the setup, execution, results, and analysis, alongside key insights and limitations identified during the experiment.

### Review and Reflection
We reflect on the experiment's outcomes, evaluating the analysis's feasibility within a constrained timeframe and identifying potential areas for future research and improvement.

## Setup Instructions

### Prerequisites
- Authorized access to the MIMIC dataset.
- Adequate computational resources for running the Meditron 7B model.

### Installation
A step-by-step guide is provided for setting up the experiment environment, covering required software, libraries, and configuration steps to prepare the system for execution.

### Running the Experiment
Detailed commands and scripts needed to run the experiment are provided, including necessary parameters and configuration options to customize the analysis.

## Contributing
We welcome contributions to extend or refine the experiment. Guidelines for contributing are provided, encouraging collaborative research and development.

## License
This experiment is shared under the MIT License, promoting open and reproducible scientific research.

## Acknowledgments
We extend our gratitude to all contributors, data providers, and supporting organizations that made this research possible.

## Contact Information
For further inquiries or contributions, please contact the primary researchers or maintainers at [your contact information].

### Additional Development
Following recent developments, the experiment is now structured for easier deployment and reproducibility, including:
- A `config.py` module for dynamic configuration management.
- A `parse_args` function in `utils/cli.py` for command-line interface enhancements.
- Packaging and installation support through a `pyproject.toml` file, facilitating the experiment's integration and distribution.
