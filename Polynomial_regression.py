{
    "nbformat": 4,
    "nbformat_minor": 0,
    "metadata": {
        "colab": {
            "provenance": []
        },
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3"
        },
        "language_info": {
            "name": "python"
        }
    },
    "cells": [
        {
            "cell_type": "markdown",
            "source": [
                "# Problem Description:\n",
                "A Human Resource company needs to determine the salary for a new job position being created. They only have access to a salary dataset for the company, which includes salary information for the top 10 positions along with their corresponding levels. The task is to assist HR in deciding the appropriate salary if the new position falls between levels 7 and 8.\n",
                "\n",
                "Data Set: **Position_Salaries.csv**\n",
                "Rules: You are restricted from utilizing the sklearn library.You are limited to using only the libraries provided.\n",
                "\n",
                "Reference : https://www.javatpoint.com/machine-learning-polynomial-regression\n",
                "\n",
                " https://www.kaggle.com/code/omkarsantoshraut/polynomial-regression"
            ],
            "metadata": {
                "id": "AtzSquaQnaBD"
            }
        },
        {
            "cell_type": "code",
            "source": [
                "# Allowded to use only these libraries\n",
                "\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import pandas as pd\n",
                "import seaborn as sns"
            ],
            "metadata": {
                "id": "1tJn4PzWnZtz"
            },
            "execution_count": null,
            "outputs": []
        },
        {
            "cell_type": "markdown",
            "source": [
                "## Exploratory data analysis"
            ],
            "metadata": {
                "id": "pDonG1iOtiCP"
            }
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {
                "id": "BUFCZbfRlfzi"
            },
            "outputs": [],
            "source": [
                "# your code(s)"
            ]
        },
        {
            "cell_type": "markdown",
            "source": [
                "### Based on the exploratory data analysis, answer the following\n",
                "\n",
                "\n",
                "* Can you use a simple linear regression model to fit this data (Yes/No)?\n",
                "> * Your answer\n",
                "* If you use a simple linear model to fit this data, will it fit well (Yes/No)?\n",
                "> * Your answer\n",
                "* Explain why you said yes or no to the above questions.\n",
                "> * Your answer\n",
                "\n"
            ],
            "metadata": {
                "id": "mvaBWQfAtpp-"
            }
        },
        {
            "cell_type": "markdown",
            "source": [
                "## Polynomial Regression\n",
                "\n",
                "**Construct a second order Model:** $$\\;\\;\\;\\;\n",
                "\\hat y = w_1 x_1^2 + w_2x_1 + b\n",
                "$$\n",
                "\n",
                "**Construct a Cost function:**\n",
                "$$MSE(w_1,w_2,b)= your\\;answer$$"
            ],
            "metadata": {
                "id": "exOvj2CxFelv"
            }
        },
        {
            "cell_type": "code",
            "source": [
                "# your code to plot the cost function (if required)"
            ],
            "metadata": {
                "id": "Da1vxqoEyL-W"
            },
            "execution_count": null,
            "outputs": []
        },
        {
            "cell_type": "markdown",
            "source": [
                "### By analysing the cost function, answer the following\n",
                "\n",
                "\n",
                "* Can you use mean squared error as the cost function (Yes/No)?\n",
                "> * Your answer\n",
                "* Explain why you said yes or no to the above questions.\n",
                "> * Your answer"
            ],
            "metadata": {
                "id": "2aQT57RJySAu"
            }
        },
        {
            "cell_type": "markdown",
            "source": [
                "**Derivatives of cost function:**\n",
                "$$Your \\; answer$$\n",
                "\n",
                "**Gradient Descent Algorithm:**\n",
                "```\n",
                "Repeat until converges:\n",
                "```\n",
                "$$your\\;answer$$"
            ],
            "metadata": {
                "id": "sTQ46QsyyuYG"
            }
        },
        {
            "cell_type": "markdown",
            "source": [
                "## Implementation of the model"
            ],
            "metadata": {
                "id": "7bzYFCh5zIL4"
            }
        },
        {
            "cell_type": "code",
            "source": [
                "# Write a code/ function to do the following\n",
                "\n",
                "# function for your model\n",
                "\n",
                "# a function for your cost function\n",
                "\n",
                "# function to calculate the derivatives\n",
                "\n",
                "# code to estimate the parametes using gradient descent\n",
                "# Aslo estimate the cost function in each iteration\n",
                "\n",
                "# Plot the model with the data given\n",
                "# plot the iteratio VS cost\n",
                "\n",
                "# estimate the solution to the given problem\n",
                "\n",
                "# mark the point or result in the graph (plot)\n",
                "\n",
                "# Estimate the model performance"
            ],
            "metadata": {
                "id": "EPZv6kMJzfk4"
            },
            "execution_count": null,
            "outputs": []
        },
        {
            "cell_type": "markdown",
            "source": [
                "### Answer the following\n",
                "\n",
                "* What is learning rate?\n",
                "> * Your answer\n",
                "* What will happen if the learning rate is too large?\n",
                "> * Your answer\n",
                "* What will happen if the learning rate is too small?\n",
                "> * Your answer\n",
                "* If you what to change the second order (quadratic) model to third order model what all things will change in the above code?\n",
                "> * Your answer\n",
                "> * Your answer\n",
                "> * Your answer\n",
                "> * Your answer\n",
                "> * Your answer"
            ],
            "metadata": {
                "id": "qhvdbzMx0P-B"
            }
        }
    ]
}