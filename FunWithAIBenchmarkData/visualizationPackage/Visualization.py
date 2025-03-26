# File Name: Visualization.py
# Name: Jay Powell
# Email: powela9@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 3/27/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment:
    # processes MMLU dataset CSVs to analyze data, generate PDFs, compute readability metrics,
    # visualize answer distributions, and display an image of a Zubat
# Brief Description of what this module does:
    # Generates a bar chart to visualize the distribution of correct answers from an MMLU dataset CSV file
# Citations:
    # https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module
    # https://www.geeksforgeeks.org/python-count-occurrences-element-list/
# Anything else that's relevant

import csv
from collections import Counter
import matplotlib.pyplot as plt

class Visualization:
    """
    Class to generate a bar chart showing the distribution of correct answers in an MMLU dataset.
    """

    def __init__(self, file_path):
        """
        Initialize with the file path of the CSV file.

        @param file_path: str - Path to the MMLU dataset CSV file.
        """
        self.file_path = file_path

    def read_correct_answers(self):
        """
        Reads the CSV file and extracts the correct answer column.

        @return: List[str] - List of correct answer choices (A, B, C, D).
        """
        correct_answers = []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 6:
                    correct_answers.append(row[5].strip())
        return correct_answers

    def plot_distribution(self):
        """
        Plots a bar chart of the distribution of correct answers.
        """
        correct_answers = self.read_correct_answers()
        answer_counts = Counter(correct_answers)

        plt.figure(figsize=(6, 4))
        plt.bar(answer_counts.keys(), answer_counts.values(), color=['blue', 'green', 'red', 'purple'])
        plt.xlabel("Answer Choice")
        plt.ylabel("Frequency")
        plt.title("Distribution of Correct Answers")
        plt.xticks(['A', 'B', 'C', 'D'])
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

        # Add to main using:
        #    file_path = "[one of the CSV files]"
        #    viz = Visualization(file_path)
        #    viz.plot_distribution()
